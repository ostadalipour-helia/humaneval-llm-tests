import os
import sys
import json
import re
import gzip
import time
from pathlib import Path
from google import genai
from tqdm import tqdm

# --- Configuration ---
DATA_PATH = Path("data/humaneval/data/HumanEval.jsonl.gz")
OUT_DIR = Path("sut_llm")
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "gemini-2.5-flash"
API_KEY = os.environ["GEMINI_API_KEY"]


# --- Initialize Gemini client ---
client = genai.Client(api_key=API_KEY)


# --- Rate Limiter ---
class RateLimiter:
    """Rate limiter to ensure we don't exceed API quota."""
    def __init__(self, max_requests_per_minute=10):
        self.max_requests = max_requests_per_minute
        self.request_times = []
    
    def wait_if_needed(self):
        """Wait if we've hit the rate limit."""
        now = time.time()
        
        # Remove requests older than 1 minute
        self.request_times = [t for t in self.request_times if now - t < 60]
        
        # If we've hit the limit, wait
        if len(self.request_times) >= self.max_requests:
            oldest_request = self.request_times[0]
            wait_time = 60 - (now - oldest_request) + 1  # +1 second buffer
            
            if wait_time > 0:
                print(f"    ⏳ Rate limit reached ({len(self.request_times)}/{self.max_requests}). Waiting {wait_time:.0f}s...")
                time.sleep(wait_time)
                
                # Clean up old requests again after waiting
                now = time.time()
                self.request_times = [t for t in self.request_times if now - t < 60]
        
        # Record this request
        self.request_times.append(time.time())


# Create rate limiter instance
rate_limiter = RateLimiter(max_requests_per_minute=10)

def save_solution_file(file_path, code):
    """Save generated solution to file."""
    try:
        # Clean the code (remove markdown markers if present)
        code = code.strip()
        if code.startswith("```"):
            code = re.sub(r"^```(?:python)?\s*", "", code)
        if code.endswith("```"):
            code = re.sub(r"\s*```$", "", code)
        code = code.strip()
        
        # Write to file
        with open(file_path, 'w') as f:
            f.write(code)
        
        return True
    except Exception as e:
        print(f"    ❌ Error saving file: {e}")
        return False



TEMPERATURE = 0.7
MAX_TOKENS = 8000

PROMPT_TEMPLATE = """You are a Python developer.
Given the following function docstring, implement the complete function.
Include all necessary imports at the top.
Return only valid Python code with no explanations or markdown formatting.

Function to implement:
{docstring}
"""

# --- Initialize Gemini client ---
client = genai.Client(api_key=API_KEY)


def clean_code(code):
    """Remove Markdown-style code block markers."""
    code = code.strip()
    
    # Remove leading ```python or ```
    if code.startswith("```"):
        code = re.sub(r"^```(?:python)?\s*", "", code)
    
    # Remove trailing ```
    if code.endswith("```"):
        code = re.sub(r"\s*```$", "", code)
    
    return code.strip()


def load_problems(data_path):
    """Load all problems from HumanEval dataset."""
    with gzip.open(data_path, "rt", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def generate_prompt(docstring):
    """Create prompt for solution generation."""
    return PROMPT_TEMPLATE.format(docstring=docstring)


def generate_solution_code(prompt):
    try:
        # Wait if needed to respect rate limit
        rate_limiter.wait_if_needed()
        
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "temperature": TEMPERATURE,
                "max_output_tokens": MAX_TOKENS
            },
        )
        
        if hasattr(response, 'text') and response.text:
            return response.text
        else:
            return None
            
    except Exception as e:
        print(f"❌ API call failed: {e}")
        return None


def main():
    problems = load_problems(DATA_PATH)
    successful = 0
    failed = 0
    
    for prob in tqdm(problems, desc="Generating LLM solutions"):
        prob_id = prob["task_id"].replace("/", "_")
        docstring = prob["prompt"]
        
        prompt = generate_prompt(docstring)
        raw_code = generate_solution_code(prompt)
        
        if raw_code:
            code = clean_code(raw_code)
            out_file = OUT_DIR / f"problem_{prob_id}.py"
            
            if save_solution_file(out_file, code):
                successful += 1
            else:
                failed += 1
        else:
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"Solution Generation Complete!")
    print(f"{'='*50}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {len(problems)}")


if __name__ == "__main__":
    main()
