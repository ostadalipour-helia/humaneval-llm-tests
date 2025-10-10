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
from datetime import datetime

# --- Configuration ---
SUT_DIR = Path("sut_llm")
TEST_DIR = Path("tests_fixed")
ENHANCED_TEST_DIR = Path("tests_enhanced")
ENHANCED_TEST_DIR.mkdir(parents=True, exist_ok=True)

RESULTS_DIR = Path("results")
LOGS_DIR = Path("results/enhancement_logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "gemini-2.5-flash"
API_KEY = os.environ["GEMINI_API_KEY"]

TEMPERATURE = 0.3
MAX_TOKENS = 8000

COVERAGE_ENHANCE_PROMPT = """You are a Python developer writing unit tests to improve code coverage.

The following code has some lines that are not covered by existing tests:

{function_code}

**Uncovered line numbers:** {uncovered_line_numbers}

**Actual uncovered lines:**
{uncovered_lines_content}

Generate ONLY test method definitions (def test_xxx) that will execute these uncovered lines.
- Generate 1-3 test methods
- Each method should be a standalone unittest method
- Use proper 4-space indentation for method body
- DO NOT include: class definitions, import statements, or if __name__ blocks
- Return ONLY the method definitions

Example format:
    def test_edge_case(self):
        result = {entry_point}(test_input)
        self.assertEqual(result, expected)

Now generate the test methods:
"""

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
                print(f"    ⏳ Rate limit reached. Waiting {wait_time:.0f}s...")
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


def load_uncovered_lines():
    """Load uncovered lines data."""
    uncovered_file = RESULTS_DIR / "uncovered_lines.json"
    if uncovered_file.exists():
        with open(uncovered_file, 'r') as f:
            return json.load(f)
    return []


def extract_entry_point(function_code):
    """Extract function name from code."""
    match = re.search(r'def (\w+)\(', function_code)
    if match:
        return match.group(1)
    return "unknown_function"


def get_uncovered_lines_content(function_code, uncovered_line_numbers):
    """Extract the actual content of uncovered lines."""
    lines = function_code.split('\n')
    uncovered_content = []
    
    for line_num in uncovered_line_numbers:
        # Convert to 0-indexed
        idx = line_num - 1
        if 0 <= idx < len(lines):
            uncovered_content.append(f"Line {line_num}: {lines[idx]}")
    
    return '\n'.join(uncovered_content) if uncovered_content else "No specific lines identified"


def save_prompt_log(problem_id, prompt, response, status, timestamp):
    """Save detailed log of prompt and response."""
    log_file = LOGS_DIR / f"{problem_id}_enhancement.json"
    
    log_entry = {
        "timestamp": timestamp,
        "problem_id": problem_id,
        "status": status,
        "prompt": prompt,
        "response": response,
        "response_length": len(response) if response else 0
    }
    
    with open(log_file, 'w') as f:
        json.dump(log_entry, f, indent=2)
    
    # Also save a human-readable version
    log_txt_file = LOGS_DIR / f"{problem_id}_enhancement.txt"
    with open(log_txt_file, 'w') as f:
        f.write(f"{'='*80}\n")
        f.write(f"COVERAGE ENHANCEMENT LOG\n")
        f.write(f"{'='*80}\n")
        f.write(f"Problem ID: {problem_id}\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Status: {status}\n")
        f.write(f"{'='*80}\n\n")
        
        f.write(f"{'='*80}\n")
        f.write(f"PROMPT\n")
        f.write(f"{'='*80}\n")
        f.write(prompt)
        f.write(f"\n\n")
        
        f.write(f"{'='*80}\n")
        f.write(f"RESPONSE\n")
        f.write(f"{'='*80}\n")
        f.write(response if response else "No response generated")
        f.write(f"\n\n")


def generate_coverage_tests(problem_id, function_code, uncovered_line_numbers, max_retries=3):
    """Generate new tests to cover uncovered lines with retry logic."""
    entry_point = extract_entry_point(function_code)
    
    # Get the actual content of uncovered lines
    uncovered_lines_content = get_uncovered_lines_content(function_code, uncovered_line_numbers)
    
    prompt = COVERAGE_ENHANCE_PROMPT.format(
        function_code=function_code,
        uncovered_line_numbers=uncovered_line_numbers,
        uncovered_lines_content=uncovered_lines_content,
        problem_id=problem_id,
        entry_point=entry_point
    )
    
    timestamp = datetime.now().isoformat()
    
    for attempt in range(max_retries):
        try:
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
                save_prompt_log(problem_id, prompt, "No response received", "no_response", timestamp)
                return None
            
            # Try to get text
            text = None
            if hasattr(response, 'text'):
                text = response.text
            elif hasattr(response, 'candidates') and response.candidates:
                candidate = response.candidates[0]
                if hasattr(candidate, 'content') and candidate.content:
                    if hasattr(candidate.content, 'parts') and candidate.content.parts:
                        parts = [p.text for p in candidate.content.parts if hasattr(p, 'text')]
                        text = ''.join(parts) if parts else None
            
            if not text or not text.strip():
                if attempt < max_retries - 1:
                    print(f"    ⚠️ Empty response, retrying ({attempt + 1}/{max_retries})...")
                    time.sleep(2)
                    continue
                save_prompt_log(problem_id, prompt, "Empty response", "empty_response", timestamp)
                return None
            
            cleaned_response = clean_code(text)
            save_prompt_log(problem_id, prompt, cleaned_response, "success", timestamp)
            return cleaned_response
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            if attempt < max_retries - 1:
                print(f"    ⚠️ Error (attempt {attempt + 1}/{max_retries}): {e}")
                time.sleep(2)
                continue
            print(f"    ❌ LLM call failed after {max_retries} attempts: {e}")
            save_prompt_log(problem_id, prompt, error_msg, "error", timestamp)
            return None
    
    return None


def add_tests_to_file(original_test_file, new_tests, problem_id):
    """Add new test methods to existing test file."""
    if not original_test_file.exists():
        return False
    
    if not new_tests or not new_tests.strip():
        return False
    
    # More strict validation
    new_tests_lower = new_tests.lower()
    if any(pattern in new_tests_lower for pattern in ['class ', 'if __name__', 'unittest.main()']):
        print(f"    ⚠️ LLM generated invalid format (contains class/main/import)")
        return False
    
    # Check if it actually contains test methods
    if 'def test_' not in new_tests:
        print(f"    ⚠️ No test methods found in generated code")
        return False
    
    original_content = original_test_file.read_text()
    
    # Find the class definition
    class_match = re.search(r'class (\w+)\(unittest\.TestCase\):', original_content)
    if not class_match:
        return False
    
    # Find where to insert (before if __name__ or at end)
    if "if __name__" in original_content:
        parts = original_content.split("if __name__")
        main_part = parts[0]
        footer = "if __name__" + parts[1]
    else:
        main_part = original_content
        footer = ""
    
    # Clean and indent the new tests
    lines = []
    for line in new_tests.split('\n'):
        stripped = line.strip()
        
        # Skip empty lines at start/end
        if not stripped:
            if lines:  # Only add if we've started adding content
                lines.append('')
            continue
            
        # Skip import lines
        if stripped.startswith('import ') or stripped.startswith('from '):
            continue
        
        # Ensure proper indentation (4 spaces for class methods)
        if stripped.startswith('def '):
            lines.append('    ' + stripped)
        elif line.startswith('    '):
            lines.append(line)
        elif line.startswith('\t'):
            lines.append('    ' + line.lstrip('\t'))
        else:
            # Inside a method, needs 8 spaces
            lines.append('        ' + stripped)
    
    if not lines:
        print(f"    ⚠️ No valid content after cleaning")
        return False
    
    new_tests_indented = '\n'.join(lines)
    
    # Combine
    enhanced_content = main_part.rstrip() + '\n\n' + new_tests_indented + '\n\n' + footer
    
    # Validate syntax
    try:
        import ast
        ast.parse(enhanced_content)
    except SyntaxError as e:
        print(f"    ⚠️ Generated code has syntax error: {str(e)[:100]}")
        return False
    
    return enhanced_content


def calculate_coverage(problem_id, test_dir):
    """Calculate code coverage for a specific problem."""
    sut_file = SUT_DIR / f"problem_{problem_id}.py"
    test_file = test_dir / f"problem_{problem_id}_gen.py"
    
    if not sut_file.exists() or not test_file.exists():
        return None
    
    try:
        # Ensure __init__.py files exist
        (SUT_DIR / "__init__.py").touch(exist_ok=True)
        (test_dir / "__init__.py").touch(exist_ok=True)
        
        # CRITICAL: Erase previous coverage data
        subprocess.run(
            [sys.executable, "-m", "coverage", "erase"],
            capture_output=True,
            timeout=5
        )
        
        # Use module path format - ONLY measure this specific file
        test_module = f"{test_dir.name}.problem_{problem_id}_gen"
        
        result = subprocess.run(
            [sys.executable, "-m", "coverage", "run",
             "--source", f"sut_llm.problem_{problem_id}",  # Only this module!
             "-m", "unittest", test_module],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=Path.cwd()
        )
        
        if result.returncode != 0:
            print(f"    ⚠️ Tests failed")
            return 0.0
        
        report = subprocess.run(
            [sys.executable, "-m", "coverage", "report"],
            capture_output=True,
            text=True
        )
        
        coverage_pct = None
        for line in report.stdout.split("\n"):
            if f"problem_{problem_id}" in line:
                parts = line.split()
                for part in parts:
                    if "%" in part:
                        coverage_pct = float(part.replace("%", ""))
                        break
        
        if coverage_pct is None:
            # Try TOTAL as fallback
            for line in report.stdout.split("\n"):
                if "TOTAL" in line:
                    parts = line.split()
                    for part in parts:
                        if "%" in part:
                            coverage_pct = float(part.replace("%", ""))
                            break
        
        if coverage_pct is None:
            coverage_pct = 0.0
        
        return coverage_pct
        
    except Exception as e:
        print(f"    ❌ Error calculating coverage: {e}")
        return None


def enhance_coverage_for_problem(problem_data):
    """Enhance coverage for a single problem."""
    problem_id = problem_data["problem_id"]
    uncovered_lines = problem_data["uncovered_lines"]
    coverage_before = problem_data.get("coverage_before_enhancement", 0)
    
    # Skip if already perfect or no data
    if coverage_before == "N/A":
        return {
            "problem_id": problem_id,
            "status": "no_coverage_data",
            "coverage_before": "N/A",
            "coverage_after": "N/A"
        }
    
    # Skip if no uncovered lines or already 100% coverage
    if not uncovered_lines or coverage_before == 100:
        return {
            "problem_id": problem_id,
            "status": "already_100",
            "coverage_before": coverage_before,
            "coverage_after": coverage_before
        }
    
    # Read function code
    sut_file = SUT_DIR / f"problem_{problem_id}.py"
    if not sut_file.exists():
        return {
            "problem_id": problem_id,
            "status": "no_sut",
            "coverage_before": coverage_before,
            "coverage_after": "N/A"
        }
    
    function_code = sut_file.read_text()
    
    # Generate new tests with retries
    print(f"    Generating tests for {len(uncovered_lines)} uncovered lines...")
    new_tests = generate_coverage_tests(problem_id, function_code, uncovered_lines, max_retries=3)
    
    if not new_tests:
        return {
            "problem_id": problem_id,
            "status": "llm_failed",
            "coverage_before": coverage_before,
            "coverage_after": coverage_before  # Keep original coverage
        }
    
    # Add to existing test file
    original_test_file = TEST_DIR / f"problem_{problem_id}_gen.py"
    enhanced_content = add_tests_to_file(original_test_file, new_tests, problem_id)
    
    if not enhanced_content:
        return {
            "problem_id": problem_id,
            "status": "merge_failed",
            "coverage_before": coverage_before,
            "coverage_after": coverage_before  # Keep original coverage
        }
    
    # Save enhanced test file
    enhanced_test_file = ENHANCED_TEST_DIR / f"problem_{problem_id}_gen.py"
    enhanced_test_file.write_text(enhanced_content)
    
    # Calculate new coverage
    coverage_after = calculate_coverage(problem_id, ENHANCED_TEST_DIR)
    
    if coverage_after is None:
        coverage_after = coverage_before
        status = "coverage_calc_failed"
    elif coverage_after < coverage_before:
        # If worse, mark as failed but keep original
        coverage_after = coverage_before
        status = "coverage_decreased"
    else:
        status = "success"
    
    return {
        "problem_id": problem_id,
        "status": status,
        "coverage_before": coverage_before,
        "coverage_after": coverage_after
    }


def main():
    print("Starting coverage enhancement...\n")
    print(f"Logs will be saved to: {LOGS_DIR}\n")
    
    # Load uncovered lines data
    uncovered_data = load_uncovered_lines()
    
    results = []
    
    for i, problem_data in enumerate(uncovered_data):
        problem_id = problem_data["problem_id"]
        print(f"[{i+1}/{len(uncovered_data)}] Enhancing coverage for {problem_id}...")
        
        result = enhance_coverage_for_problem(problem_data)
        results.append(result)
        
        print(f"  Coverage: {result['coverage_before']}% → {result['coverage_after']}%")
        print()
    
    # Save results
    import csv
    with open(RESULTS_DIR / "coverage_improvement.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["problem_id", "status", 
                                                "coverage_before", "coverage_after"])
        writer.writeheader()
        writer.writerows(results)
    
    # Print summary
    valid_results = [r for r in results if r["coverage_after"] != "N/A" and r["coverage_before"] != "N/A"]
    
    if valid_results:
        avg_before = sum(r["coverage_before"] for r in valid_results) / len(valid_results)
        avg_after = sum(r["coverage_after"] for r in valid_results) / len(valid_results)
        improvement = avg_after - avg_before
        
        print("\n" + "="*50)
        print("COVERAGE ENHANCEMENT COMPLETE!")
        print("="*50)
        print(f"Problems processed: {len(results)}")
        print(f"Average coverage before: {avg_before:.2f}%")
        print(f"Average coverage after: {avg_after:.2f}%")
        print(f"Average improvement: {improvement:.2f}%")
        print(f"Results saved to: results/coverage_improvement.csv")
        print(f"Detailed logs saved to: {LOGS_DIR}")


if __name__ == "__main__":
    main()