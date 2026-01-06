import os
import json
import re
import time
import ast
from pathlib import Path
from google import genai
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from google.api_core.exceptions import ResourceExhausted, ServiceUnavailable
from tqdm import tqdm

# ============================================================
# CONFIG (aligned with your spec generator)
# ============================================================
ROOT = Path(__file__).resolve().parents[1]

SPEC_DIR = ROOT / "specs"
OUT_DIR = ROOT / "tests_spec"
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "gemini-2.5-flash"
MAX_TOKENS = 8000

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=API_KEY)

sut_path = Path(f"sut/problem_{problem_id}.py")
sut_code = sut_path.read_text()

# Load the function into Python so we can compute outputs
namespace = {}
exec(sut_code, namespace)
solution_fn = namespace[list(namespace.keys())[-1]]   # last function defined



# ============================================================
# RATE LIMITER (same style as your pipeline)
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
            print(f"⏳ Rate limit hit, waiting {wait:.0f}s…")
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
    wait=wait_fixed(4),
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
# CLEAN LLM CODE
# ============================================================
def clean_code(code):
    code = code.strip()

    # Remove markdown fences if present
    if code.startswith("```"):
        code = re.sub(r"^```(?:python)?\s*", "", code)
    if code.endswith("```"):
        code = re.sub(r"\s*```$", "", code)

    return code.strip()


# ============================================================
# PROMPT TEMPLATE (test generation from spec)
# ============================================================
TEST_GENERATION_PROMPT = """
You are generating Python unittest test cases from a specification.

SPECIFICATION (JSON):
{spec_json}

REQUIREMENTS:
- Write a full unittest test file.
- Include import statements.
- Create ONE test class named Test_{entry_point}.
- Write 6–12 test methods.
- Include normal cases, edge cases, and error cases.
- Error cases must use assertRaises with correct exception.
- DO NOT invent behavior not in the spec.
- Use ONLY Python code. No markdown, no explanations.

FORMAT STRICTLY:
1. import unittest
2. from sut.problem_{task_id} import {entry_point}
3. class Test_{entry_point}(unittest.TestCase):
       def test_xxx(self):
           ...

Do NOT return anything except pure Python code.
"""


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("\n📘 Generating tests from specs...\n")

    spec_files = sorted(SPEC_DIR.glob("HumanEval_*_spec.json"))

    for spec_file in tqdm(spec_files, desc="Generating spec-based tests"):
        task_id = spec_file.stem.replace("_spec", "")
        spec_json = json.loads(spec_file.read_text())

        entry_point = spec_json["entry_point"]
        prompt = TEST_GENERATION_PROMPT.format(
            spec_json=json.dumps(spec_json, indent=2),
            task_id=task_id,
            entry_point=entry_point,
        )

        out_path = OUT_DIR / f"{task_id}_gen.py"
        if out_path.exists():
            print(f"➡️ {task_id} already exists — skipping")
            continue

        try:
            raw = call_llm(prompt)
            cleaned = clean_code(raw)

            # Validate Python syntax BEFORE saving
            try:
                ast.parse(cleaned)
            except Exception as e:
                print(f"❌ Invalid Python code for {task_id}: {e}")
                continue

            out_path.write_text(cleaned)
            print(f"✅ Saved: {out_path}")

        except Exception as e:
            print(f"❌ Failed for {task_id}: {e}")
            continue

    print("\n🎉 DONE — tests saved in spec_pipeline/tests_spec/\n")
