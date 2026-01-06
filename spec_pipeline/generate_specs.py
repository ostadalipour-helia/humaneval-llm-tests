import os
from google import genai
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from pathlib import Path
import json, gzip, time, re
from google.api_core.exceptions import ResourceExhausted, ServiceUnavailable


# ============================================================
# CONFIG
# ============================================================
ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "humaneval" / "data" / "HumanEval.jsonl.gz"
OUTPUT_DIR = Path("specs")
OUTPUT_DIR.mkdir(exist_ok=True)

MODEL_NAME = "gemini-2.5-flash"
MAX_TOKENS = 8000

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not set")

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
            print(f"⏳ Rate limit hit — waiting {wait:.0f}s...")
            time.sleep(wait)
        self.times.append(time.time())

rate_limiter = RateLimiter()


# ============================================================
# JSON REPAIR + RECONSTRUCTION
# ============================================================
def try_fix_json(raw_text, problem_id, original_docstring):
    """
    Attempts:
    1. Clean + direct JSON parse
    2. LLM JSON repair on the broken JSON
    3. Fallback: rebuild JSON from the REAL docstring
    """

    cleaned = raw_text.strip()
    cleaned = cleaned.replace("```json", "").replace("```", "").strip()

    # Replace single quotes
    cleaned = cleaned.replace("'", '"')

    # Strip trailing commas
    cleaned = re.sub(r",\s*([\]}])", r"\1", cleaned)

    # ----------------------
    # FIRST ATTEMPT
    # ----------------------
    try:
        return json.loads(cleaned)
    except:
        pass

    # ----------------------
    # SECOND ATTEMPT: repair the broken JSON
    # ----------------------
    repair_prompt = f"""
Fix this invalid JSON so it becomes VALID STRICT JSON.
No comments. No explanations. JSON only.

Broken JSON:
{cleaned}
"""
    try:
        rate_limiter.wait_if_needed()
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=repair_prompt,
            config={"temperature": 0.0, "max_output_tokens": 5000},
        )

        if hasattr(response, "text") and response.text:
            repaired = response.text
        else:
            repaired = "".join(
                p.text for p in response.candidates[0].content.parts
                if hasattr(p, "text")
            )

        repaired = repaired.strip("`").strip()

        try:
            return json.loads(repaired)
        except:
            print(f"⚠️ LLM repair attempt failed for {problem_id}")
    except Exception as e:
        print(f"⚠️ JSON repair error for {problem_id}: {e}")

    # ----------------------
    # THIRD ATTEMPT: FULL RECONSTRUCTION
    # ----------------------
    fallback_prompt = f"""
JSON is corrupted beyond repair.

REBUILD a NEW STRICT JSON SPEC from scratch.
DO NOT EXPLAIN. JSON ONLY.

Target structure:
{{
  "task_id": "{problem_id}",
  "entry_point": "",
  "preconditions": [],
  "postconditions": [],
  "invariants": [],
  "normal_cases": [],
  "edge_cases": [],
  "error_conditions": []
}}

Use ONLY the REAL HumanEval DOCSTRING:

DOCSTRING:
{original_docstring}
"""

    try:
        rate_limiter.wait_if_needed()
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=fallback_prompt,
            config={"temperature": 0.0, "max_output_tokens": 6000},
        )

        if hasattr(response, "text") and response.text:
            rebuilt = response.text
        else:
            rebuilt = "".join(
                p.text for p in response.candidates[0].content.parts
                if hasattr(p, "text")
            )

        rebuilt = rebuilt.strip("`").strip()

        return json.loads(rebuilt)

    except Exception as e:
        print(f"❌ FINAL FAIL for {problem_id}: {e}")
        return None


# ============================================================
# LOAD HumanEval
# ============================================================
def load_humaneval():
    with gzip.open(DATA_PATH, "rt", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


# ============================================================
# SAFE RESPONSE TEXT EXTRACTION
# ============================================================
def extract_text(response):
    if hasattr(response, "text") and response.text:
        return response.text.strip()
    if hasattr(response, "candidates") and response.candidates:
        parts = []
        for p in response.candidates[0].content.parts:
            if hasattr(p, "text"):
                parts.append(p.text)
        if parts:
            return "\n".join(parts).strip()
    raise RuntimeError("Empty LLM response")


# ============================================================
# LLM CALL (with retry)
# ============================================================
@retry(
    stop=stop_after_attempt(8),
    wait=wait_fixed(5),
    retry=retry_if_exception_type((RuntimeError, ServiceUnavailable, ResourceExhausted)),
)
def call_llm(prompt: str):
    rate_limiter.wait_if_needed()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={"temperature": 0.0, "max_output_tokens": MAX_TOKENS},
    )
    text = extract_text(response)
    if not text:
        raise RuntimeError("Empty LLM response — retrying")
    return text


# ============================================================
# SPECIFICATION PROMPT
# ============================================================
SPEC_PROMPT = """
You are given a function description (docstring) from the HumanEval benchmark.

Produce a STRICT JSON specification in the following format:

{{
  "task_id": "",
  "entry_point": "",
  "preconditions": [],
  "postconditions": [],
  "invariants": [],
  "normal_cases": [],
  "edge_cases": [],
  "error_conditions": []
}}

Rules:
- STRICT JSON ONLY (no explanation, no markdown)
- Double-quoted keys and strings
- No comments

DOCSTRING:
{docstring}
"""


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("📘 Generating specs with full JSON-repair + fallback reconstruction...\n")

    for problem in load_humaneval():
        task_id = problem["task_id"].replace("/", "_")
        entry = problem["entry_point"]
        docstring = problem["prompt"]

        out_path = OUTPUT_DIR / f"{task_id}_spec.json"
        if out_path.exists():
            print(f"➡️ {task_id} already exists — skipping.")
            continue

        print(f"🧠 Generating spec for {task_id}...")

        try:
            raw = call_llm(SPEC_PROMPT.format(docstring=docstring)).strip("`").strip()

            # Extract JSON region
            s = raw.find("{")
            e = raw.rfind("}")
            if s != -1 and e != -1:
                raw_json = raw[s:e+1].strip()
            else:
                raw_json = raw

            # Try direct parse → if fails → full repair
            try:
                spec = json.loads(raw_json)
            except:
                spec = try_fix_json(raw_json, task_id, docstring)

            if spec is None:
                print(f"❌ Completely failed for {task_id}\n")
                continue

            spec["task_id"] = task_id
            spec["entry_point"] = entry

            out_path.write_text(json.dumps(spec, indent=2))
            print(f"✅ Saved: {out_path}\n")

        except Exception as e:
            print(f"❌ Failed for {task_id}: {e}\n")
            continue
