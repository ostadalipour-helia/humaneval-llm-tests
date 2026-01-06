import unittest
import sys
import csv
from pathlib import Path
import gzip
import json
import subprocess
import shutil
import time

# ============================================================
# CONFIG
# ============================================================
TEST_DIR = Path("tests_spec/NoSUT_Baseline")     # spec-based tests
SUT_DIR = Path("sut")             # canonical SUTs
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# LOAD ALL HUMAN-EVAL PROBLEM IDS
# ============================================================
def load_problem_ids():
    DATA_PATH = Path("data/humaneval/data/HumanEval.jsonl.gz")
    ids = []
    with gzip.open(DATA_PATH, "rt", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            ids.append(obj["task_id"].replace("/", "_"))
    return ids


# ============================================================
# VALIDITY RATE (with timeout and safety)
# ============================================================
def calculate_validity_rate(problem_id):
    test_file = TEST_DIR / f"problem_{problem_id}_gen.py"

    if not test_file.exists():
        print(f"  Missing test file for {problem_id}")
        return None, 0, 0

    try:
        result = subprocess.run(
            [sys.executable, "-m", "unittest", str(test_file)],
            capture_output=True,
            text=True,
            timeout=30,            # safety timeout
        )
        output = result.stderr + result.stdout

        if "Ran" not in output:
            return None, 0, 0

        total = 0
        for line in output.split("\n"):
            if "Ran" in line:
                try:
                    total = int(line.split()[1])
                except:
                    return None, 0, 0

        failed = output.count("FAIL") + output.count("ERROR")
        passing = max(0, total - failed)
        validity = (passing / total * 100) if total > 0 else None

        return validity, passing, total

    except subprocess.TimeoutExpired:
        print(f"  Validity timed out for {problem_id}")
        return None, 0, 0

    except Exception as e:
        print(f"  Error running validity for {problem_id}: {e}")
        return None, 0, 0


# ============================================================
# COVERAGE (with timeout and safety)
# ============================================================
def calculate_coverage(problem_id):
    sut_file = SUT_DIR / f"problem_{problem_id}.py"
    test_file = TEST_DIR / f"problem_{problem_id}_gen.py"

    if not sut_file.exists() or not test_file.exists():
        return None

    try:
        subprocess.run(
            [sys.executable, "-m", "coverage", "erase"],
            capture_output=True,
        )

        subprocess.run(
            [sys.executable, "-m", "coverage", "run",
             "--source", "sut",
             "-m", "unittest", str(test_file)],
            capture_output=True,
            text=True,
            timeout=30,     # safety timeout
        )

        report = subprocess.run(
            [sys.executable, "-m", "coverage", "report"],
            capture_output=True,
            text=True,
        )

        for line in report.stdout.split("\n"):
            if f"problem_{problem_id}" in line:
                for part in line.split():
                    if "%" in part:
                        return float(part.replace("%", ""))

        return None

    except subprocess.TimeoutExpired:
        print(f"  Coverage timed out for {problem_id}")
        return None

    except Exception as e:
        print(f"  Coverage failed for {problem_id}: {e}")
        return None


# ============================================================
# MUTATION SCORE — SAFE & SKIPPABLE
# ============================================================
def get_passing_tests(problem_id):
    test_file = TEST_DIR / f"problem_{problem_id}_gen.py"

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=no"],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except Exception:
        return []

    passed = []
    for line in result.stdout.split("\n"):
        if " PASSED" in line:
            passed.append(line.split("::")[-1].split()[0])
    return passed


def clear_mutmut_cache():
    cache = Path(".mutmut-cache")
    if cache.exists():
        try:
            if cache.is_dir():
                shutil.rmtree(cache)
            else:
                cache.unlink()
        except Exception:
            # safe ignore
            pass


def calculate_mutation_score(problem_id):
    sut_file = SUT_DIR / f"problem_{problem_id}.py"
    test_file = TEST_DIR / f"problem_{problem_id}_gen.py"

    passing = get_passing_tests(problem_id)
    if not passing:
        print(f"  No passing tests for {problem_id} — skipping mutation.")
        return None

    selector = " or ".join(passing)

    try:
        clear_mutmut_cache()

        result = subprocess.run(
            [
                sys.executable, "-m", "mutmut", "run",
                "--paths-to-mutate", str(sut_file),
                "--tests-dir", str(TEST_DIR),
                "--runner",
                f"python -m pytest {test_file} -k '{selector}' -x --tb=no -q",
            ],
            capture_output=True,
            text=True,
            timeout=300,    # mutation takes longer
        )

        out = result.stdout + result.stderr

        killed = survived = timeout_c = suspicious = 0

        for line in out.split("\n"):
            if "🎉" in line or "🙁" in line:
                parts = line.split()
                for i, part in enumerate(parts):
                    try:
                        if "🎉" in part:
                            killed = int(parts[i+1])
                        if "🙁" in part:
                            survived = int(parts[i+1])
                        if "⏰" in part:
                            timeout_c = int(parts[i+1])
                        if "🤔" in part:
                            suspicious = int(parts[i+1])
                    except:
                        pass

        total = killed + survived + timeout_c + suspicious
        if total == 0:
            return None

        return (killed / total) * 100

    except subprocess.TimeoutExpired:
        print(f"  Mutation timed out for {problem_id}")
        return None

    except Exception as e:
        print(f"  Mutation error for {problem_id}: {e}")
        return None


# ============================================================
# MAIN
# ============================================================
def main():
    print("📘 Evaluating spec-based test suite...\n")

    ids = load_problem_ids()
    results = []

    for i, pid in enumerate(ids):
        print(f"[{i+1}/{len(ids)}] Evaluating {pid}...")

        validity, passed, total = calculate_validity_rate(pid)
        print(f"  Validity: {validity}% ({passed}/{total})")

        coverage = calculate_coverage(pid)
        print(f"  Coverage: {coverage}%")

        # ----------------------------------------------------
        # SAFETY: SKIP MUTATION FOR INVALID/TIMEOUT CASES
        # ----------------------------------------------------
        if validity is None or total == 0 or coverage is None:
            print(f"  Skipping mutation for {pid} due to invalid tests or timeout.")
            mutation = None
        else:
            mutation = calculate_mutation_score(pid)

        print(f"  Mutation: {mutation}%\n")

        results.append({
            "problem_id": pid,
            "validity_rate": validity,
            "passing_tests": passed,
            "total_tests": total,
            "coverage": coverage,
            "mutation_score": mutation,
        })

    # Save metrics
    out_file = RESULTS_DIR / "metrics_spec_hybrid.csv"
    with open(out_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "problem_id",
                "validity_rate",
                "passing_tests",
                "total_tests",
                "coverage",
                "mutation_score",
            ],
        )
        writer.writeheader()
        writer.writerows(results)

    print("\n🎉 DONE — results saved to results/metrics_spec.csv\n")


if __name__ == "__main__":
    main()
