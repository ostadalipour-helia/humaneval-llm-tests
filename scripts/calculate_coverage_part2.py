import sys
import subprocess
import gzip
import json
import csv
import ast
from pathlib import Path

DATA_PATH = Path("data/humaneval/data/HumanEval.jsonl.gz")
SUT_DIR = Path("sut_llm")
TEST_DIR = Path("tests_fixed")
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def load_problem_ids():
    """Load all problem IDs from dataset."""
    with gzip.open(DATA_PATH, "rt", encoding="utf-8") as f:
        problem_ids = []
        for line in f:
            obj = json.loads(line)
            task_id = obj["task_id"].replace("/", "_")
            problem_ids.append(task_id)
        return problem_ids


def calculate_coverage(problem_id):
    """Calculate code coverage for a problem."""
    sut_file = SUT_DIR / f"problem_{problem_id}.py"
    test_file = TEST_DIR / f"problem_{problem_id}_gen.py"
    
    if not sut_file.exists():
        print(f"  ⚠️ SUT file not found")
        return None, []
        
    if not test_file.exists():
        print(f"  ⚠️ Test file not found")
        return None, []
    
    # Check if SUT file has valid syntax
    try:
        with open(sut_file, 'r') as f:
            ast.parse(f.read())
    except SyntaxError as e:
        print(f"  ❌ SUT has syntax error (LLM generation failed)")
        return None, []
    
    try:
        # Ensure __init__.py files exist
        (SUT_DIR / "__init__.py").touch(exist_ok=True)
        (TEST_DIR / "__init__.py").touch(exist_ok=True)
        
        # CRITICAL: Erase previous coverage data
        subprocess.run(
            [sys.executable, "-m", "coverage", "erase"],
            capture_output=True,
            timeout=5
        )
        
        # Run coverage ONLY measuring this specific file
        test_module = f"{TEST_DIR.name}.problem_{problem_id}_gen"
        
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
            print(f"  ⚠️ Tests failed")
            return 0.0, []
        
        # Get coverage report
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
            
        # Get uncovered lines
        uncovered_lines = []
        annotate_result = subprocess.run(
            [sys.executable, "-m", "coverage", "annotate", str(sut_file)],
            capture_output=True,
            text=True
        )
        
        annotated_file = Path(str(sut_file) + ",cover")
        if annotated_file.exists():
            with open(annotated_file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    if line.startswith("!"):
                        uncovered_lines.append(line_num)
            annotated_file.unlink()
        
        return coverage_pct, uncovered_lines
    
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return None, []

def main():
    print("Calculating coverage after fixing...\n")
    
    problem_ids = load_problem_ids()
    results = []
    
    syntax_errors = 0
    successful = 0
    failed = 0
    
    for i, problem_id in enumerate(problem_ids):
        print(f"[{i+1}/{len(problem_ids)}] Calculating coverage for {problem_id}...")
        
        coverage_pct, uncovered_lines = calculate_coverage(problem_id)
        
        if coverage_pct is None:
            failed += 1
            # Check if it was due to syntax error
            sut_file = SUT_DIR / f"problem_{problem_id}.py"
            if sut_file.exists():
                try:
                    with open(sut_file, 'r') as f:
                        ast.parse(f.read())
                except SyntaxError:
                    syntax_errors += 1
        else:
            successful += 1
            print(f"  Coverage: {coverage_pct}%")
            print(f"  Uncovered lines: {len(uncovered_lines)}")
        
        results.append({
            "problem_id": problem_id,
            "coverage_before_enhancement": coverage_pct if coverage_pct is not None else "N/A",
            "uncovered_lines": uncovered_lines
        })
        
        print()
    
    # Save results
    with open(RESULTS_DIR / "coverage_before_enhancement.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["problem_id", "coverage_before_enhancement"])
        writer.writeheader()
        for r in results:
            writer.writerow({
                "problem_id": r["problem_id"],
                "coverage_before_enhancement": r["coverage_before_enhancement"]
            })
    
    # Save uncovered lines for enhancement
    with open(RESULTS_DIR / "uncovered_lines.json", "w") as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    valid_coverage = [r["coverage_before_enhancement"] for r in results 
                     if r["coverage_before_enhancement"] != "N/A"]
    
    print("\n" + "="*50)
    print("COVERAGE CALCULATION COMPLETE!")
    print("="*50)
    print(f"Total problems: {len(problem_ids)}")
    print(f"Successfully calculated: {successful}")
    print(f"Failed: {failed}")
    print(f"  - Due to syntax errors: {syntax_errors}")
    print(f"  - Due to other errors: {failed - syntax_errors}")
    
    if valid_coverage:
        print(f"\nAverage Coverage: {sum(valid_coverage)/len(valid_coverage):.2f}%")
        print(f"Min Coverage: {min(valid_coverage):.2f}%")
        print(f"Max Coverage: {max(valid_coverage):.2f}%")
    
    print(f"\nResults saved to: results/coverage_before_enhancement.csv")
    
    # Show which problems had syntax errors
    syntax_error_problems = []
    for r in results:
        if r["coverage_before_enhancement"] == "N/A":
            problem_id = r["problem_id"]
            sut_file = SUT_DIR / f"problem_{problem_id}.py"
            if sut_file.exists():
                try:
                    with open(sut_file, 'r') as f:
                        ast.parse(f.read())
                except SyntaxError:
                    syntax_error_problems.append(problem_id)
    
    if syntax_error_problems:
        print(f"\n⚠️  Problems with syntax errors in LLM-generated code:")
        for pid in syntax_error_problems:
            print(f"   - {pid}")


if __name__ == "__main__":
    main()