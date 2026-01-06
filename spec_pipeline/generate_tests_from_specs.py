import os
import json
import time
import ast
import re
from pathlib import Path
from google import genai
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from google.api_core.exceptions import ResourceExhausted, ServiceUnavailable
from tqdm import tqdm

# ============================================================
# CONFIG
# ============================================================
ROOT = Path(__file__).resolve().parents[1]

SPEC_DIR = ROOT / "specs"
OUT_DIR = ROOT / "tests_spec"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SUT_DIR = ROOT / "sut"

MODEL_NAME = "gemini-2.5-pro"
MAX_TOKENS = 8000

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=API_KEY)


# ============================================================
# RATE LIMITER
# ============================================================
class RateLimiter:
    def __init__(self, max_rpm=10):
        self.max_rpm = max_rpm
        self.times = []

    def wait_if_needed(self):
        now = time.time()
        self.times = [t for t in self.times if now - t < 60]
        if len(self.times) >= self.max_rpm:
            wait = 60 - (now - self.times[0]) + 1
            print(f"⏳ Rate limit reached. Waiting {wait:.0f}s…")
            time.sleep(wait)
        self.times.append(time.time())


rate_limiter = RateLimiter()


# ============================================================
# RESPONSE EXTRACTION
# ============================================================
def extract_text(resp):
    if hasattr(resp, "text") and resp.text:
        return resp.text
    if hasattr(resp, "candidates") and resp.candidates:
        parts = []
        for p in resp.candidates[0].content.parts:
            if hasattr(p, "text"):
                parts.append(p.text)
        return "\n".join(parts)
    return ""


# ============================================================
# LLM CALL
# ============================================================
@retry(
    stop=stop_after_attempt(5),
    wait=wait_fixed(3),
    retry=retry_if_exception_type((RuntimeError, ServiceUnavailable, ResourceExhausted)),
)
def call_llm(prompt):
    rate_limiter.wait_if_needed()
    resp = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={"temperature": 0.0, "max_output_tokens": MAX_TOKENS},
    )
    text = extract_text(resp)
    if not text:
        raise RuntimeError("Empty LLM response")
    return text


# ============================================================
# CLEAN PYTHON CODE
# ============================================================
def clean_code(code):
    code = code.strip()

    if code.startswith("```"):
        code = re.sub(r"^```(?:python)?", "", code, flags=re.MULTILINE).strip()
    if code.endswith("```"):
        code = re.sub(r"```$", "", code).strip()

    return code.strip()


# ============================================================
# PROMPT TEMPLATE
# ============================================================
TEST_GENERATION_PROMPT = """
You are generating Python unittest test cases using:

1. The HumanEval specification
2. The REAL Python implementation of the function
3. PRE-CALCULATED true outputs for specific inputs

You MUST produce a correct unittest file using ONLY these inputs & outputs.

========================
### SPECIFICATION (JSON)
========================
{spec_json}

==============================
### PRECOMPUTED TRUE OUTPUTS
==============================
COMPUTED_CASES = {computed_cases_json}

Use EXACT values from expected_output_repr.

========================
### ERROR CASES (IF ANY)
========================
ERROR_CASES = {error_cases_json}

===========================
### FUNCTION IMPLEMENTATION
===========================
```python
{sut_code}
```

====================================
### STRICT RULES
====================================
- Use ONLY inputs from COMPUTED_CASES and ERROR_CASES.
- Use EXACT expected outputs provided.
- DO NOT invent new inputs.
- DO NOT invent new behavior.
- DO NOT modify expected outputs.
- Generate **10 test methods**.
- Output ONLY Python code. No markdown, no comments.

====================================
### REQUIRED FORMAT
====================================
import unittest
from sut.problem_{task_id} import {entry_point}

class Test_{entry_point}(unittest.TestCase):
    def test_xxx(self):
        ...

Return ONLY valid Python code.
"""


# ============================================================
# COMPUTE TRUE OUTPUTS FROM REAL SUT
# ============================================================
def compute_outputs(spec_json, solution_fn):
    computed = []

    for case in spec_json.get("normal_cases", []) + spec_json.get("edge_cases", []):
        if "input" not in case:
            continue

        inp = case["input"]

        # Convert input into args/kwargs
        if isinstance(inp, list):
            args = inp
            kwargs = {}
        elif isinstance(inp, dict):
            args = []
            kwargs = inp
        else:
            args = [inp]
            kwargs = {}

        try:
            out = solution_fn(*args, **kwargs)
            out_repr = repr(out)
        except Exception as e:
            out_repr = f"EXC:{repr(e)}"

        computed.append({
            "input": inp,
            "expected_output_repr": out_repr
        })

    return computed


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("\n📘 Generating SPEC-based tests (using REAL SUT outputs)…\n")

    spec_files = sorted(SPEC_DIR.glob("HumanEval_*_spec.json"))

    for spec_file in tqdm(spec_files, desc="Generating tests"):
        task_id = spec_file.stem.replace("_spec", "")
        spec_json = json.loads(spec_file.read_text())
        entry_point = spec_json["entry_point"]

        # ---------------------------
        # Load SUT implementation
        # ---------------------------
        sut_file = SUT_DIR / f"problem_{task_id}.py"
        if not sut_file.exists():
            print(f"⚠️ Missing SUT for {task_id}")
            continue

        sut_code = sut_file.read_text()

        namespace = {}
        try:
            exec(sut_code, namespace)
        except Exception as e:
            print(f"❌ SUT execution error for {task_id}: {e}")
            continue

        if entry_point not in namespace:
            print(f"❌ Entry point {entry_point} not found for {task_id}")
            continue

        solution_fn = namespace[entry_point]

        # ---------------------------
        # Compute real SUT outputs
        # ---------------------------
        computed_cases = compute_outputs(spec_json, solution_fn)
        error_cases = spec_json.get("error_cases", [])

        if not computed_cases and not error_cases:
            print(f"⚠️ No usable cases in spec for {task_id}")
            continue

        # ---------------------------
        # Build prompt
        # ---------------------------
        prompt = TEST_GENERATION_PROMPT.format(
            spec_json=json.dumps(spec_json, indent=2),
            computed_cases_json=json.dumps(computed_cases, indent=2),
            error_cases_json=json.dumps(error_cases, indent=2),
            sut_code=sut_code,
            task_id=task_id,
            entry_point=entry_point,
        )

        out_path = OUT_DIR / f"{task_id}_gen.py"
        if out_path.exists():
            print(f"➡️ {task_id} already exists — skipping")
            continue

        # ---------------------------
        # LLM call
        # ---------------------------
        try:
            raw = call_llm(prompt)
            cleaned = clean_code(raw)

            try:
                ast.parse(cleaned)
            except Exception as e:
                print(f"❌ Invalid Python code for {task_id}: {e}")
                continue

            out_path.write_text(cleaned)
            print(f"✅ Saved: {out_path}")

        except Exception as e:
            print(f"❌ LLM error for {task_id}: {e}")
            continue

    print("\n🎉 Done! Tests saved to tests_spec/\n")
