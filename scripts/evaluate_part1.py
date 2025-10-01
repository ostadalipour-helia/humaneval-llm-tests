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

def calculate_mutation_score(problem_id):
    """Calculate mutation score using mutmut"""
    sut_file = Path(f"sut/problem_{problem_id}.py")
    test_file = Path(f"tests/problem_{problem_id}_gen.py")
    
    if not sut_file.exists() or not test_file.exists():
        return None
    
    try:
        # Ensure directories are Python packages
        Path("sut/__init__.py").touch(exist_ok=True)
        Path("tests/__init__.py").touch(exist_ok=True)
        
        # Clean previous mutmut cache - handle both file and directory
        cache_path = Path(".mutmut-cache")
        if cache_path.exists():
            if cache_path.is_file():
                cache_path.unlink()  # Remove file
            else:
                shutil.rmtree(cache_path)  # Remove directory
        
        # Create setup.cfg for this specific problem
        config = f"""[mutmut]
paths_to_mutate=sut/problem_{problem_id}.py
runner=pytest tests/problem_{problem_id}_gen.py -x --tb=no -q
"""
        with open("setup.cfg", "w") as f:
            f.write(config)
        
        # Run mutmut with increased timeout
        result = subprocess.run(
            [sys.executable, "-m", "mutmut", "run"],
            capture_output=True,
            text=True,
            timeout=180
        )
        
        # Get results
        results = subprocess.run(
            [sys.executable, "-m", "mutmut", "results"],
            capture_output=True,
            text=True
        )
        
        output = results.stdout
        
        # Parse mutmut 2.4.0 output format
        killed = survived = timeout_count = suspicious = 0
        
        # Try to parse from the summary line
        for line in result.stdout.split('\n'):
            if '🎉' in line and '🙁' in line:
                parts = line.split()
                for i, part in enumerate(parts):
                    if '🎉' in part and i+1 < len(parts):
                        try:
                            killed = int(parts[i+1])
                        except ValueError:
                            pass
                    elif '🙁' in part and i+1 < len(parts):
                        try:
                            survived = int(parts[i+1])
                        except ValueError:
                            pass
                    elif '⏰' in part and i+1 < len(parts):
                        try:
                            timeout_count = int(parts[i+1])
                        except ValueError:
                            pass
                    elif '🤔' in part and i+1 < len(parts):
                        try:
                            suspicious = int(parts[i+1])
                        except ValueError:
                            pass
        
        total = killed + survived + timeout_count + suspicious
        
        if total > 0:
            mutation_score = (killed / total) * 100
            print(f"  Mutation details: {killed} killed, {survived} survived, {timeout_count} timeout, {suspicious} suspicious")
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
