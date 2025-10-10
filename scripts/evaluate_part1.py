import unittest
import sys
import csv
from pathlib import Path
import gzip
import json
import subprocess
import shutil

def load_problem_ids():
    """Load all problem IDs from dataset"""
    DATA_PATH = Path("data/humaneval/data/HumanEval.jsonl.gz")
    problem_ids = []
    
    with gzip.open(DATA_PATH, "rt", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            task_id = obj["task_id"].replace("/", "_")
            problem_ids.append(task_id)
    
    return problem_ids

def calculate_validity_rate(problem_id):
    """Calculate validity rate by running tests against ground-truth solution"""
    test_file = Path(f"tests/problem_{problem_id}_gen.py")
    
    if not test_file.exists():
        return None, 0, 0
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "unittest", str(test_file)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = result.stderr + result.stdout
        
        if "Ran" in output:
            for line in output.split("\n"):
                if "Ran" in line:
                    try:
                        total = int(line.split()[1])
                        failed = output.count("FAIL") + output.count("ERROR")
                        passing = total - failed
                        validity_rate = (passing / total * 100) if total > 0 else 0
                        return validity_rate, passing, total
                    except:
                        pass
        
        return None, 0, 0
    
    except Exception as e:
        print(f"  Error in validity test for {problem_id}: {e}")
        return None, 0, 0

def calculate_coverage(problem_id):
    """Calculate code coverage"""
    sut_file = Path(f"sut/problem_{problem_id}.py")
    test_file = Path(f"tests/problem_{problem_id}_gen.py")
    
    if not sut_file.exists() or not test_file.exists():
        return None
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "coverage", "run", "--source", f"sut", 
             "-m", "unittest", str(test_file)],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=Path.cwd()
        )
        
        report = subprocess.run(
            [sys.executable, "-m", "coverage", "report"],
            capture_output=True,
            text=True
        )
        
        for line in report.stdout.split("\n"):
            if "problem_" + problem_id in line:
                parts = line.split()
                for part in parts:
                    if "%" in part:
                        return float(part.replace("%", ""))
        
        if "TOTAL" in report.stdout:
            for line in report.stdout.split("\n"):
                if "TOTAL" in line:
                    parts = line.split()
                    for part in parts:
                        if "%" in part:
                            return float(part.replace("%", ""))
        
        return 0.0
    
    except Exception as e:
        print(f"  Error in coverage for {problem_id}: {e}")
        return None

def get_passing_tests(problem_id):
    """Identify which tests pass"""
    test_file = Path(f"tests/problem_{problem_id}_gen.py")
    
    # Run tests and capture which ones pass
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=no"],
        capture_output=True,
        text=True,
        timeout=30
    )
    
    passing_tests = []
    for line in result.stdout.split('\n'):
        if ' PASSED' in line:
            # Extract test name: "test_file.py::TestClass::test_name PASSED"
            test_name = line.split('::')[-1].split(' ')[0]
            passing_tests.append(test_name)
    
    return passing_tests


def calculate_mutation_score(problem_id):
    """Calculate mutation score using only passing tests"""
    sut_file = Path(f"sut/problem_{problem_id}.py")
    test_file = Path(f"tests/problem_{problem_id}_gen.py")
    
    if not sut_file.exists() or not test_file.exists():
        return None
    
    try:
        # Get list of passing tests
        passing_tests = get_passing_tests(problem_id)
        
        if not passing_tests:
            print(f"  No passing tests for {problem_id}")
            return 0.0
        
        # Clean cache
        cache_path = Path(".mutmut-cache")
        if cache_path.exists():
            if cache_path.is_file():
                cache_path.unlink()
            else:
                shutil.rmtree(cache_path)
        
        # Build test selection string for pytest
        # Format: "test_name1 or test_name2 or test_name3"
        test_selector = " or ".join(passing_tests)
        
        # Run mutmut with only passing tests
        result = subprocess.run(
            [
                sys.executable, "-m", "mutmut", "run",
                "--paths-to-mutate", f"sut/problem_{problem_id}.py",
                "--tests-dir", "tests/",
                "--runner", f"python -m pytest tests/problem_{problem_id}_gen.py -k '{test_selector}' -x --tb=no -q"
            ],
            capture_output=True,
            text=True,
            timeout=180
        )
        
        # Parse output...
        output = result.stdout + result.stderr
        
        killed = survived = timeout_count = suspicious = 0
        
        for line in output.split('\n'):
            if '🎉' in line or '🙁' in line:
                parts = line.split()
                for i, part in enumerate(parts):
                    if '🎉' in part and i+1 < len(parts):
                        try:
                            killed = int(parts[i+1])
                        except (ValueError, IndexError):
                            pass
                    elif '🙁' in part and i+1 < len(parts):
                        try:
                            survived = int(parts[i+1])
                        except (ValueError, IndexError):
                            pass
                    elif '⏰' in part and i+1 < len(parts):
                        try:
                            timeout_count = int(parts[i+1])
                        except (ValueError, IndexError):
                            pass
                    elif '🤔' in part and i+1 < len(parts):
                        try:
                            suspicious = int(parts[i+1])
                        except (ValueError, IndexError):
                            pass
        
        total = killed + survived + timeout_count + suspicious
        
        if total > 0:
            mutation_score = (killed / total) * 100
            print(f"  Mutation details: {killed} killed, {survived} survived, {timeout_count} timeout, {suspicious} suspicious")
            print(f"  (Using {len(passing_tests)} passing tests out of total)")
            return mutation_score
        
        print(f"  Warning: No mutations found for {problem_id}")
        return 0.0
        
    except subprocess.TimeoutExpired:
        print(f"  Mutation testing timed out for {problem_id}")
        return None
    except Exception as e:
        print(f"  Error in mutation testing for {problem_id}: {e}")
        return None


def main():
    print("Starting evaluation of Part 1...\n")
    
    problem_ids = load_problem_ids()
    results = []
    
    Path("results").mkdir(parents=True, exist_ok=True)
    Path("results/coverage").mkdir(parents=True, exist_ok=True)
    
    for i, problem_id in enumerate(problem_ids):
        print(f"[{i+1}/{len(problem_ids)}] Evaluating {problem_id}...")
        
        validity_rate, passing, total = calculate_validity_rate(problem_id)
        print(f"  Validity Rate: {validity_rate}% ({passing}/{total})")
        
        coverage = calculate_coverage(problem_id)
        print(f"  Coverage: {coverage}%")
        
        mutation_score = calculate_mutation_score(problem_id)
        print(f"  Mutation Score: {mutation_score}%")
        
        results.append({
            "problem_id": problem_id,
            "validity_rate": validity_rate if validity_rate is not None else "N/A",
            "passing_tests": passing,
            "total_tests": total,
            "coverage": coverage if coverage is not None else "N/A",
            "mutation_score": mutation_score if mutation_score is not None else "N/A"
        })
        
        print()
    
    with open("results/metrics.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["problem_id", "validity_rate", 
                                                "passing_tests", "total_tests",
                                                "coverage", "mutation_score"])
        writer.writeheader()
        writer.writerows(results)
    
    print("\n" + "="*50)
    print("EVALUATION COMPLETE!")
    print("="*50)
    print(f"Results saved to: results/metrics.csv")
    print(f"Total problems evaluated: {len(results)}")
    
    valid_validity = [r["validity_rate"] for r in results if r["validity_rate"] != "N/A"]
    valid_coverage = [r["coverage"] for r in results if r["coverage"] != "N/A"]
    valid_mutation = [r["mutation_score"] for r in results if r["mutation_score"] != "N/A"]
    
    if valid_validity:
        print(f"Average Validity Rate: {sum(valid_validity)/len(valid_validity):.2f}%")
    if valid_coverage:
        print(f"Average Coverage: {sum(valid_coverage)/len(valid_coverage):.2f}%")
    if valid_mutation:
        print(f"Average Mutation Score: {sum(valid_mutation)/len(valid_mutation):.2f}%")

if __name__ == "__main__":
    main()