import os
import sys
import json
import gzip
import subprocess
import re
import time
from pathlib import Path
from google import genai
from tqdm import tqdm

# --- Configuration ---
DATA_PATH = Path("data/humaneval/data/HumanEval.jsonl.gz")
SUT_DIR = Path("sut_llm")
TEST_DIR = Path("tests")
FIXED_TEST_DIR = Path("tests_fixed")
FIXED_TEST_DIR.mkdir(parents=True, exist_ok=True)

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "gemini-2.5-flash"
API_KEY = os.environ["GEMINI_API_KEY"]

TEMPERATURE = 0.0
MAX_TOKENS = 8000
MAX_FIX_ATTEMPTS = 3

# FIXED: Use triple quotes without f-string
FIX_PROMPT_TEMPLATE = """You are a Python developer fixing a failing unit test.

Function being tested:
{function_code}

Failing test code:
{test_code}

Error message:
{error_message}

Fix the test code to make it correct. The test logic may be wrong, or the assertions may be incorrect.
Return ONLY the corrected test method code (the single test_xxx method), with no explanations or markdown.
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
                print(f"        ⏳ Rate limit reached. Waiting {wait_time:.0f}s...")
                time.sleep(wait_time)
                
                # Clean up old requests again after waiting
                now = time.time()
                self.request_times = [t for t in self.request_times if now - t < 60]
        
        # Record this request
        self.request_times.append(time.time())


# Create rate limiter instance
rate_limiter = RateLimiter(max_requests_per_minute=10)


def clean_code(code):
    """Remove Markdown-style code block markers."""
    code = code.strip()
    if code.startswith("```"):
        code = re.sub(r"^```(?:python)?\s*", "", code)
    if code.endswith("```"):
        code = re.sub(r"\s*```$", "", code)
    return code.strip()


def load_problem_ids():
    """Load all problem IDs from dataset."""
    with gzip.open(DATA_PATH, "rt", encoding="utf-8") as f:
        problem_ids = []
        for line in f:
            obj = json.loads(line)
            task_id = obj["task_id"].replace("/", "_")
            problem_ids.append(task_id)
        return problem_ids


def run_single_test(test_file, test_method):
    """Run a single test method and capture output."""
    try:
        # Get the test class name from the file
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Find the test class name
        class_match = re.search(r'class (\w+)\(unittest\.TestCase\):', content)
        if not class_match:
            return False, "No TestCase class found in test file"
        
        test_class_name = class_match.group(1)
        
        # Get the module path relative to tests_fixed directory
        test_module = f"tests_fixed.{test_file.stem}"
        
        # DEBUG: Print test execution details
        full_test_path = f"{test_module}.{test_class_name}.{test_method}"
        print(f"      DEBUG: Running test: {full_test_path}")
        
        result = subprocess.run(
            [sys.executable, "-m", "unittest", full_test_path],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=Path.cwd()  # Run from project root
        )
        
        output = result.stderr + result.stdout
        passed = result.returncode == 0
        
        return passed, output
        
    except subprocess.TimeoutExpired:
        return False, "Test execution timeout after 10 seconds"
    except FileNotFoundError:
        return False, "Test file or module not found"
    except Exception as e:
        return False, f"Test execution error: {str(e)}"


def extract_test_methods(test_file_path):
    """Extract individual test methods from a test file."""
    with open(test_file_path, 'r') as f:
        content = f.read()
    
    # Find all test methods
    pattern = r'(def (test_\w+)\(self\):.*?)(?=\n    def |\nif __name__|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    test_methods = {}
    for full_match, method_name in matches:
        test_methods[method_name] = full_match.strip()
    
    return test_methods


def read_function_code(problem_id):
    """Read the LLM-generated function code."""
    sut_file = SUT_DIR / f"problem_{problem_id}.py"
    if sut_file.exists():
        return sut_file.read_text()
    return ""


def fix_test_with_llm(function_code, test_code, error_message, max_retries=3):
    """Use LLM to fix a failing test with retry logic."""
    # FIXED: Now the .format() will actually work because we're not using f-string
    prompt = FIX_PROMPT_TEMPLATE.format(
        function_code=function_code,
        test_code=test_code,
        error_message=error_message
    )
    

    
    for retry in range(max_retries):
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
            
            # DEBUG: Print response object details
            print(f"\n{'='*60}")
            print(f"DEBUG: Response object (attempt {retry+1}):")
            print(f"{'='*60}")
            print(f"Type: {type(response)}")
            
            # Check finish reason and safety ratings
            if hasattr(response, 'candidates') and response.candidates:
                candidate = response.candidates[0]
                print(f"First candidate type: {type(candidate)}")
                
                # Check finish reason
                if hasattr(candidate, 'finish_reason'):
                    print(f"Finish reason: {candidate.finish_reason}")
                
                # Check safety ratings
                if hasattr(candidate, 'safety_ratings'):
                    print(f"Safety ratings: {candidate.safety_ratings}")
                
                # Check content structure
                print(f"Has .content: {hasattr(candidate, 'content')}")
                if hasattr(candidate, 'content'):
                    print(f"Content type: {type(candidate.content)}")
                    print(f"Content is None: {candidate.content is None}")
                    if candidate.content:
                        print(f"Has .parts: {hasattr(candidate.content, 'parts')}")
                        if hasattr(candidate.content, 'parts'):
                            print(f"Parts is None: {candidate.content.parts is None}")
                            if candidate.content.parts:
                                print(f"Parts length: {len(candidate.content.parts)}")
            
            print(f"Has .text: {hasattr(response, 'text')}")
            print(f"{'='*60}\n")
            
            # Extract text from response - try multiple methods with safety checks
            raw_response = None
            
            # Method 1: Try .text attribute directly
            if hasattr(response, 'text'):
                try:
                    raw_response = response.text
                except:
                    pass
            
            # Method 2: Try to get text from candidates
            if not raw_response and hasattr(response, 'candidates') and response.candidates:
                try:
                    candidate = response.candidates[0]
                    if hasattr(candidate, 'content') and candidate.content is not None:
                        if hasattr(candidate.content, 'parts') and candidate.content.parts is not None:
                            # Extract text from parts
                            parts_text = []
                            for part in candidate.content.parts:
                                if hasattr(part, 'text') and part.text:
                                    parts_text.append(part.text)
                            if parts_text:
                                raw_response = ''.join(parts_text)
                except Exception as e:
                    print(f"    ⚠️ Error extracting from candidates: {e}")
            
            # DEBUG: Print raw AI response
            print(f"\n{'='*60}")
            print(f"DEBUG: Raw AI Response (attempt {retry+1}):")
            print(f"{'='*60}")
            print(f"Response is None: {raw_response is None}")
            if raw_response:
                print(raw_response)
            else:
                print("⚠️ NO TEXT RETURNED FROM API")
                print("This might be due to:")
                print("  - Content filtering/safety filters")
                print("  - API rate limiting")
                print("  - API issues")
                
                # Check if we can get more info from the response
                if hasattr(response, 'candidates') and response.candidates:
                    candidate = response.candidates[0]
                    if hasattr(candidate, 'finish_reason'):
                        print(f"  - Finish reason: {candidate.finish_reason}")
            print(f"{'='*60}\n")
            
            if not raw_response:
                print(f"    ⚠️ Empty response from API on attempt {retry+1}")
                if retry < max_retries - 1:
                    continue
                else:
                    return None
            
            # Clean and return
            cleaned_response = clean_code(raw_response)
            
            # DEBUG: Print cleaned response if different
            if cleaned_response != raw_response:
                print(f"\n{'='*60}")
                print("DEBUG: Cleaned AI Response:")
                print(f"{'='*60}")
                print(cleaned_response)
                print(f"{'='*60}\n")
            
            return cleaned_response
            
        except Exception as e:
            error_msg = str(e)
            print(f"\n{'='*60}")
            print(f"DEBUG: Exception occurred:")
            print(f"{'='*60}")
            print(f"Error type: {type(e).__name__}")
            print(f"Error: {e}")
            import traceback
            print(f"Traceback:\n{traceback.format_exc()}")
            print(f"{'='*60}\n")
            
            if "Connection reset" in error_msg or "timeout" in error_msg.lower():
                if retry < max_retries - 1:
                    print(f"    ⚠️ Network error (attempt {retry+1}/{max_retries}): {e}")
                    continue
            
            print(f"    ❌ LLM fix failed: {e}")
            return None
    
    print(f"    ❌ LLM fix failed after {max_retries} retries")
    return None


def update_test_in_file(test_file_content, old_test_code, new_test_code):
    """Replace old test code with new test code in file content."""
    # Try to find and replace the test method
    if old_test_code in test_file_content:
        return test_file_content.replace(old_test_code, new_test_code)
    else:
        # If exact match fails, try to find by method name
        old_method_name = re.search(r'def (test_\w+)\(self\):', old_test_code)
        if old_method_name:
            method_name = old_method_name.group(1)
            # Find and replace the entire method
            pattern = rf'(    def {method_name}\(self\):.*?)(?=\n    def |\nif __name__|$)'
            return re.sub(pattern, new_test_code, test_file_content, flags=re.DOTALL)
    
    return test_file_content


def fix_tests_for_problem(problem_id):
    """Fix all failing tests for a single problem."""
    test_file = TEST_DIR / f"problem_{problem_id}_gen.py"
    
    if not test_file.exists():
        return {
            "problem_id": problem_id,
            "status": "no_test_file",
            "total_tests": 0,
            "fixed": 0,
            "discarded": 0,
            "passed_initially": 0
        }
    
    # Read original test file 
    original_content = test_file.read_text()
    # Update imports from sut to sut_llm
    original_content = original_content.replace(f"from sut.problem_{problem_id}", f"from sut_llm.problem_{problem_id}")
    current_content = original_content
    
    # Extract test methods
    test_methods = extract_test_methods(test_file)
    
    # Read function code
    function_code = read_function_code(problem_id)
    
    if not function_code:
        return {
            "problem_id": problem_id,
            "status": "no_sut_file",
            "total_tests": len(test_methods),
            "fixed": 0,
            "discarded": 0,
            "passed_initially": 0
        }
    
    stats = {
        "problem_id": problem_id,
        "total_tests": len(test_methods),
        "fixed": 0,
        "discarded": 0,
        "passed_initially": 0,
        "test_details": []
    }
    
    # Create temp test file in tests_fixed directory
    temp_test_file = FIXED_TEST_DIR / f"problem_{problem_id}_gen_temp.py"
    
    for method_name, test_code in test_methods.items():
        print(f"    Testing: {method_name}")
        
        # Write current content to temp file in tests_fixed - UPDATE IMPORTS
        updated_temp_content = current_content.replace(
            f"from sut.problem_{problem_id}",
            f"from sut_llm.problem_{problem_id}"
        )
        temp_test_file.write_text(updated_temp_content)
        
        # Run the test
        passed, output = run_single_test(temp_test_file, method_name)
        
        if passed:
            print(f"      ✅ Passed")
            stats["passed_initially"] += 1
            stats["test_details"].append({
                "test_name": method_name,
                "status": "passed_initially"
            })
            continue
        
        # Test failed, try to fix
        print(f"      ❌ Failed, attempting to fix...")
        
        fixed = False
        for attempt in range(1, MAX_FIX_ATTEMPTS + 1):
            print(f"        Attempt {attempt}/{MAX_FIX_ATTEMPTS}")
            
            # Get fixed test code from LLM
            fixed_test_code = fix_test_with_llm(function_code, test_code, output)
            
            if not fixed_test_code:
                break
            
            # Update test in content
            new_content = update_test_in_file(current_content, test_code, fixed_test_code)
            # Update imports when writing
            updated_new_content = new_content.replace(
                f"from sut.problem_{problem_id}",
                f"from sut_llm.problem_{problem_id}"
            )
            temp_test_file.write_text(updated_new_content)
            
            # Run again
            passed, output = run_single_test(temp_test_file, method_name)
            
            if passed:
                print(f"        ✅ Fixed on attempt {attempt}")
                current_content = new_content
                test_code = fixed_test_code  # Update for next iteration
                stats["fixed"] += 1
                stats["test_details"].append({
                    "test_name": method_name,
                    "status": "fixed",
                    "attempts": attempt
                })
                fixed = True
                break
        
        if not fixed:
            print(f"        ❌ Could not fix, discarding test")
            # Remove the test from content
            pattern = rf'    def {method_name}\(self\):.*?(?=\n    def |\nif __name__|$)'
            current_content = re.sub(pattern, '', current_content, flags=re.DOTALL)
            stats["discarded"] += 1
            stats["test_details"].append({
                "test_name": method_name,
                "status": "discarded"
            })
    
    # Save fixed test file - UPDATE IMPORTS
    fixed_test_file = FIXED_TEST_DIR / f"problem_{problem_id}_gen.py"

    # Update import statements from sut to sut_llm
    updated_content = current_content.replace(
        f"from sut.problem_{problem_id}",
        f"from sut_llm.problem_{problem_id}"
    )

    fixed_test_file.write_text(updated_content)
    
    # Clean up temp file
    if temp_test_file.exists():
        temp_test_file.unlink()
    
    stats["status"] = "completed"
    return stats


def main():
    print("Starting iterative test fixing...\n")
    
    problem_ids = load_problem_ids()
    all_stats = []
    
    for i, problem_id in enumerate(problem_ids):
        print(f"[{i+1}/{len(problem_ids)}] Fixing tests for {problem_id}...")
        
        stats = fix_tests_for_problem(problem_id)
        all_stats.append(stats)
        
        print(f"  Total: {stats['total_tests']}, "
              f"Passed: {stats['passed_initially']}, "
              f"Fixed: {stats['fixed']}, "
              f"Discarded: {stats['discarded']}\n")
    
    # Save results
    with open(RESULTS_DIR / "fixing_log.json", "w") as f:
        json.dump(all_stats, f, indent=2)
    
    # Print summary
    total_tests = sum(s['total_tests'] for s in all_stats)
    total_passed = sum(s['passed_initially'] for s in all_stats)
    total_fixed = sum(s['fixed'] for s in all_stats)
    total_discarded = sum(s['discarded'] for s in all_stats)
    
    print("\n" + "="*50)
    print("TEST FIXING COMPLETE!")
    print("="*50)
    print(f"Total tests: {total_tests}")
    print(f"Passed initially: {total_passed} ({total_passed/total_tests*100:.2f}%)")
    print(f"Fixed: {total_fixed} ({total_fixed/total_tests*100:.2f}%)")
    print(f"Discarded: {total_discarded} ({total_discarded/total_tests*100:.2f}%)")
    print(f"Final passing: {total_passed + total_fixed} ({(total_passed + total_fixed)/total_tests*100:.2f}%)")


if __name__ == "__main__":
    main()