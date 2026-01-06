import sys
import csv
import json
import gzip
import subprocess
import shutil
from pathlib import Path
import re

########################################################
# 📌 PROJECT ROOT
########################################################

ROOT = Path(__file__).resolve().parents[2]

TEST_DIR = ROOT / "spec_pipeline" / "tests_spec" / "SUT"
SUT_DIR = ROOT / "baseline" / "sut"
DATA_PATH = ROOT / "humaneval" / "data" / "HumanEval.jsonl.gz"
OUTPUT_CSV = ROOT / "result_spec" / f"metrics_SUT.csv"

TEST_PATTERN = "{id}_gen.py"

########################################################
# FIX IMPORT PATH SO `from sut.*` WORKS
########################################################

sys.path.append(str(ROOT))                   # /humaneval-llm-tests
sys.path.append(str(ROOT / "baseline"))      # /baseline
sys.path.append(str(ROOT / "baseline" / "sut"))
sys.path.append(str(ROOT / "humaneval"))     # if needed

########################################################
# HELPERS
########################################################

def run(cmd, timeout=60):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)

def load_problem_ids():
    ids = []
    with gzip.open(DATA_PATH, "rt", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            ids.append(obj["task_id"].replace("/", "_"))
    return ids

def test_file_for(pid):
    return TEST_DIR / TEST_PATTERN.format(id=pid)

def sut_file_for(pid):
    return SUT_DIR / f"problem_{pid}.py"

########################################################
# VALIDITY
########################################################

def calculate_validity(pid):
    test_file = test_file_for(pid)
    if not test_file.exists():
        return None, 0, 0

    res = run([sys.executable, "-m", "unittest", str(test_file)])
    output = res.stdout + res.stderr

    m = re.search(r"Ran (\d+) test", output)
    if not m:
        return None, 0, 0

    total = int(m.group(1))
    failed = 0

    m2 = re.search(r"failures=(\d+)", output)
    if m2:
        failed += int(m2.group(1))

    m3 = re.search(r"errors=(\d+)", output)
    if m3:
        failed += int(m3.group(1))

    if "OK" in output:
        failed = 0

    passing = total - failed
    validity = (passing / total) * 100 if total > 0 else 0

    return validity, passing, total

########################################################
# COVERAGE
########################################################

def calculate_coverage(pid):
    sut_path = sut_file_for(pid)
    test_path = test_file_for(pid)
    if not sut_path.exists() or not test_path.exists():
        return None

    run([sys.executable, "-m", "coverage", "erase"])
    run([
        sys.executable, "-m", "coverage", "run",
        "--source", str(sut_path),
        "-m", "unittest", str(test_path)
    ])
    res = run([sys.executable, "-m", "coverage", "report", str(sut_path)])
    out = res.stdout

    for line in out.splitlines():
        if f"problem_{pid}" in line:
            parts = line.split()
            for p in parts:
                if p.endswith("%"):
                    return float(p.replace("%", ""))
    return 0.0

########################################################
# MUTATION
########################################################

def get_passing_tests(pid):
    test_file = test_file_for(pid)
    res = run([sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=no"])
    names = []
    for line in res.stdout.splitlines():
        if " PASSED" in line:
            names.append(line.split("::")[-1].split()[0])
    return names

def clear_mutmut():
    cache = Path(".mutmut-cache")
    if cache.exists():
        if cache.is_dir(): shutil.rmtree(cache)
        else: cache.unlink()

def compute_mutation(pid):
    sut = sut_file_for(pid)
    test = test_file_for(pid)
    if not sut.exists() or not test.exists():
        return None

    passing = get_passing_tests(pid)
    if not passing:
        return 0.0

    selector = " or ".join(passing)
    clear_mutmut()

    run([
        sys.executable, "-m", "mutmut", "run",
        "--paths-to-mutate", str(sut),
        "--tests-dir", str(TEST_DIR),
        "--runner",
        f"python -m pytest {test} -k '{selector}' --tb=no -q"
    ], timeout=300)

    res = run([sys.executable, "-m", "mutmut", "results"])
    out = res.stdout

    killed = survived = timeout = suspicious = 0

    for line in out.splitlines():
        low = line.lower()
        if "killed" in low: killed += 1
        elif "survived" in low: survived += 1
        elif "timeout" in low: timeout += 1
        elif "suspicious" in low: suspicious += 1

    total = killed + survived + timeout + suspicious
    if total == 0:
        return 0.0

    return (killed / total) * 100

########################################################
# MAIN
########################################################

def main():
    print(f"\n🔍 Evaluating SUT tests at:\n{TEST_DIR}\n")

    OUTPUT_CSV.parent.mkdir(exist_ok=True)
    ids = load_problem_ids()
    results = []

    for i, pid in enumerate(ids, start=1):
        print(f"\n[{i}/{len(ids)}] {pid}")

        validity, passing, total = calculate_validity(pid)
        print(f"  Validity: {validity}% ({passing}/{total})")

        coverage = calculate_coverage(pid)
        print(f"  Coverage: {coverage}%")

        mutation = compute_mutation(pid)
        print(f"  Mutation: {mutation}%")

        results.append({
            "problem_id": pid,
            "validity_rate": validity,
            "passing_tests": passing,
            "total_tests": total,
            "coverage": coverage,
            "mutation_score": mutation,
        })

    with OUTPUT_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "problem_id","validity_rate","passing_tests",
            "total_tests","coverage","mutation_score"
        ])
        writer.writeheader()
        writer.writerows(results)

    print("\n===================================")
    print(f"  DONE — Results saved to: {OUTPUT_CSV}")
    print("===================================\n")


if __name__ == "__main__":
    main()
