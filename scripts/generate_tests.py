import os
import json
import gzip
from pathlib import Path
from google import genai
from tqdm import tqdm
import re

# --- Configuration ---
DATA_PATH = Path("data/humaneval/data/HumanEval.jsonl.gz")
OUT_DIR = Path("tests")
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "gemini-2.5-flash"
API_KEY = os.environ["GEMINI_API_KEY"]

TEMPERATURE = 0.0
MAX_TOKENS = 800

PROMPT_TEMPLATE = """You are a Python developer. 
Given only the following function docstring (no solution), 
write a Python unit test file that contains exactly 10 deterministic unit tests 
for the function using Python's unittest framework.

Requirements:
- Only import the function using: `from sut.problem_{id} import {entry_point}`
- Create a TestCase class with 10 test_... methods.
- Each test must assert the correct expected output.
- Do NOT include any solution code or explanations — output only valid Python source.

Function docstring:
\"\"\"{docstring}\"\"\"
"""

# --- Initialize Gemini client ---
client = genai.Client(api_key=API_KEY)

import re

def clean_code(code):
    """
    Remove Markdown-style code block markers like ```python ... ``` 
    from the start and end of Gemini responses.
    """
    code = code.strip()

    # Remove leading ```python or ``` with optional whitespace
    if code.startswith("```"):
        code = re.sub(r"^```(?:python)?\s*", "", code)

    # Remove trailing ```
    if code.endswith("```"):
        code = re.sub(r"\s*```$", "", code)

    return code.strip()


def load_problems(data_path):
    with gzip.open(data_path, "rt", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def generate_prompt(prob_id, entry_point, docstring):
    return PROMPT_TEMPLATE.format(id=prob_id, entry_point=entry_point, docstring=docstring)


def generate_test_code(prompt):
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "temperature": TEMPERATURE,
                "max_output_tokens": MAX_TOKENS
            },
        )
        return response.text or response.output_text
    except Exception as e:
        print(f"❌ API call failed: {e}")
        return None


def save_test_file(file_path, code):
    file_path.write_text(code)
    try:
        compile(code, str(file_path), "exec")
    except SyntaxError as e:
        print(f"⚠️ Syntax error in {file_path.name}: {e}")


def main():
    problems = load_problems(DATA_PATH)

    for prob in tqdm(problems, desc="Generating tests"):
        prob_id = prob["task_id"].replace("/", "_")
        entry_point = prob["entry_point"]
        docstring = prob["prompt"]

        prompt = generate_prompt(prob_id, entry_point, docstring)
        raw_code = generate_test_code(prompt)
        code = clean_code(raw_code) if raw_code else None



        if code:
            out_file = OUT_DIR / f"problem_{prob_id}_gen.py"
            save_test_file(out_file, code)


if __name__ == "__main__":
    main()
