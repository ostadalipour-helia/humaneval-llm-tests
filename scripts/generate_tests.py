import os
import json
import gzip
import time
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
MAX_TOKENS = 9000

PROMPT_TEMPLATE = """You are a Python developer writing comprehensive unit tests.
Given only the following function docstring (no solution), write a Python unit test file 
that contains exactly 10 deterministic unit tests for the function using Python's unittest framework.

Your tests must be designed to catch code mutations and subtle bugs. Focus on:

CRITICAL TESTING REQUIREMENTS:
1. **Boundary Testing**: Test exact boundaries (e.g., if condition uses '<', test with equal values)
   - For comparisons: test both sides of < > <= >= == !=
   - For ranges: test first element, last element, one before, one after
   
2. **Off-by-One Errors**: Test with n, n-1, n+1 for any numeric parameters
   - Array indices: first, last, middle positions
   - Loop boundaries: empty, single element, two elements
   
3. **Logic Mutations**: Test conditions that would break if AND/OR are swapped
   - Test cases where only one condition is true
   - Test cases where both/all conditions are true/false
   
4. **Return Value Testing**: Test all possible return paths
   - Early returns vs final returns
   - Default values vs computed values
   
5. **Sign and Zero Testing**: For numeric functions
   - Test with positive, negative, and zero values
   - Test with very small and very large numbers
   
6. **Edge Cases**:
   - Empty collections (list, string, dict)
   - Single element collections
   - Null/None values where applicable
   - Duplicate values
   - Collections with all same values

SPECIFIC TEST COVERAGE:
- At least 2 tests for boundary conditions
- At least 2 tests for edge cases (empty, single element)
- At least 2 tests for typical/expected inputs
- At least 2 tests for extreme or unusual inputs
- At least 2 tests that verify the exact output (not just type/truthiness)

Requirements:
- Only import the function using: `from sut.problem_{id} import {entry_point}`
- Create a TestCase class with 10 test_... methods
- Each test must assert the EXACT expected output, not just assertTrue/assertFalse
- Use assertEqual, assertListEqual, etc. to check exact values
- DO NOT include any solution code or explanations — output only valid Python source

Function docstring:
\"\"\"{docstring}\"\"\"

Generate tests that would catch mutations like:
- Changing < to <=
- Changing + to -
- Changing 0 to 1
- Changing and to or
- Changing return True to return False
"""

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
                time.sleep(wait_time)
                
                # Clean up old requests again after waiting
                now = time.time()
                self.request_times = [t for t in self.request_times if now - t < 60]
        
        # Record this request
        self.request_times.append(time.time())


# Create rate limiter instance
rate_limiter = RateLimiter(max_requests_per_minute=10)


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


def generate_test_code(prompt, max_retries=3):
    """Generate test code with retry logic and better error handling."""
    for attempt in range(max_retries):
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
            
            # Better response handling
            if not response:
                if attempt < max_retries - 1:
                    print(f"    ⚠️ No response, retrying ({attempt + 1}/{max_retries})...")
                    time.sleep(2)
                    continue
                return None
            
            # Try to get text from response
            text = None
            if hasattr(response, 'text'):
                try:
                    text = response.text
                except Exception as e:
                    print(f"    ⚠️ Error accessing response.text: {e}")
            
            # If .text doesn't work, try to extract from candidates
            if not text and hasattr(response, 'candidates') and response.candidates:
                try:
                    candidate = response.candidates[0]
                    if hasattr(candidate, 'content') and candidate.content:
                        if hasattr(candidate.content, 'parts') and candidate.content.parts:
                            parts = [p.text for p in candidate.content.parts if hasattr(p, 'text')]
                            text = ''.join(parts) if parts else None
                except Exception as e:
                    print(f"    ⚠️ Error extracting from candidates: {e}")
            
            if not text or not text.strip():
                if attempt < max_retries - 1:
                    print(f"    ⚠️ Empty response, retrying ({attempt + 1}/{max_retries})...")
                    time.sleep(2)
                    continue
                return None
            
            return text
            
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"    ⚠️ Error (attempt {attempt + 1}/{max_retries}): {e}")
                time.sleep(2)
                continue
            print(f"    ❌ API call failed after {max_retries} attempts: {e}")
            return None
    
    return None


def save_test_file(file_path, code):
    file_path.write_text(code)
    try:
        compile(code, str(file_path), "exec")
    except SyntaxError as e:
        print(f"⚠️ Syntax error in {file_path.name}: {e}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate unit tests for HumanEval problems')
    parser.add_argument('--problem', type=str, help='Generate test for specific problem (e.g., HumanEval_145)')
    parser.add_argument('--start', type=int, help='Start from problem index (0-163)')
    parser.add_argument('--end', type=int, help='End at problem index (0-163)')
    parser.add_argument('--skip-existing', action='store_true', help='Skip problems that already have test files')
    
    args = parser.parse_args()
    
    problems = load_problems(DATA_PATH)
    
    # Filter problems based on arguments
    if args.problem:
        problems = [p for p in problems if p["task_id"].replace("/", "_") == args.problem]
        if not problems:
            print(f"❌ Problem {args.problem} not found!")
            return
        print(f"Generating test for: {args.problem}")
    elif args.start is not None or args.end is not None:
        start = args.start if args.start is not None else 0
        end = args.end if args.end is not None else len(problems)
        problems = problems[start:end]
        print(f"Generating tests for problems {start} to {end-1}")
    
    successful = 0
    failed = 0
    skipped = 0

    for prob in tqdm(problems, desc="Generating tests"):
        prob_id = prob["task_id"].replace("/", "_")
        
        out_file = OUT_DIR / f"problem_{prob_id}_gen.py"
        
        # Skip if file exists and flag is set
        if args.skip_existing and out_file.exists():
            skipped += 1
            continue
        
        entry_point = prob["entry_point"]
        docstring = prob["prompt"]

        prompt = generate_prompt(prob_id, entry_point, docstring)
        raw_code = generate_test_code(prompt, max_retries=3)
        
        if raw_code:
            code = clean_code(raw_code)
            
            if code:
                save_test_file(out_file, code)
                successful += 1
            else:
                failed += 1
                print(f"❌ Failed to clean code for {prob_id}")
        else:
            failed += 1
            print(f"❌ Failed to generate code for {prob_id}")
    
    print(f"\n{'='*50}")
    print(f"Test Generation Complete!")
    print(f"{'='*50}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    if skipped > 0:
        print(f"Skipped: {skipped}")
    print(f"Total: {len(problems)}")


if __name__ == "__main__":
    main()