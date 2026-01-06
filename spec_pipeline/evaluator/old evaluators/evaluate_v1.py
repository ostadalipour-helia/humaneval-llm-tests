import sys
import csv
import json
import gzip
import re
import shutil
import subprocess
from pathlib import Path

# ==========================================
# 🔧 CONFIGURATION – EDIT THESE ONLY
# ==========================================

from pathlib import Path

# ROOT of the entire project (humaneval-llm-tests/)
ROOT = Path(__file__).resolve().parents[2]

TEST_DIR = ROOT / "spec_pipeline" / "tests_spec" / "NoSUT"
SUT_DIR = ROOT / "baseline" / "sut"
DATA_PATH = ROOT / "humaneval" / "data" / "HumanEval.jsonl.gz"
OUTPUT_CSV = ROOT / "result_spec" / f"metrics_{TEST_DIR.name}_SUT.csv"



# Pattern for each test file in TEST_DIR
# e.g. "problem_{id}_gen.py" or "{id}_gen.py"
TEST_FILE_PATTERN = "{id}_gen.py"



# Turn this on for extra logging
DEBUG = True

# ==========================================


def dbg(msg: str):
    if DEBUG:
        print(msg)


def load_problem_ids():
    """Load all HumanEval problem IDs like 'HumanEval_0', 'HumanEval_1', ..."""
    problem_ids = []
    with gzip.open(DATA_PATH, "rt", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            task_id = obj["task_id"].replace("/", "_")  # "HumanEval/0" -> "HumanEval_0"
            problem_ids.append(task_id)
    return problem_ids


def sut_file_for(problem_id: str) -> Path:
    return SUT_DIR / f"problem_{problem_id}.py"


def test_file_for(problem_id: str) -> Path:
    file_name = TEST_FILE_PATTERN.format(id=problem_id)
    return TEST_DIR / file_name


def run_cmd(cmd, timeout=60):
    """Helper to run a subprocess and return (stdout, stderr, returncode)."""
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return result.stdout, result.stderr, result.returncode


# ==========================================
# ✅ VALIDITY (test pass rate)
# ==========================================
def calculate_validity_rate(problem_id: str):
    test_file = test_file_for(problem_id)
    if not test_file.exists():
        dbg(f"  [VALIDITY] Missing test file: {test_file}")
        return None, 0, 0

    dbg(f"  [VALIDITY] Running unittest on {test_file}")
    stdout, stderr, rc = run_cmd(
        [sys.executable, "-m", "unittest", str(test_file)]
    )

    output = stdout + stderr
    # dbg("--- unittest output ---\n" + output + "\n-------------------------")

    total = None
    for line in output.splitlines():
        if line.strip().startswith("Ran "):
            parts = line.strip().split()
            # "Ran 18 tests in 0.01s"
            try:
                total = int(parts[1])
            except Exception:
                pass
            break

    failed = output.count("FAIL") + output.count("ERROR")

    if total is None or total == 0:
        return None, 0, 0

    passing = total - failed
    validity_rate = (passing / total) * 100.0
    return validity_rate, passing, total


# ==========================================
# ✅ COVERAGE (per-problem)
# ==========================================
def clear_coverage():
    # coverage erase
    run_cmd([sys.executable, "-m", "coverage", "erase"], timeout=30)


def calculate_coverage(problem_id: str):
    sut_file = sut_file_for(problem_id)
    test_file = test_file_for(problem_id)

    if not sut_file.exists() or not test_file.exists():
        dbg(f"  [COVERAGE] Missing sut or test for {problem_id}")
        return None

    clear_coverage()

    # Only track this single sut file via --source
    dbg(f"  [COVERAGE] Running coverage for {problem_id}")
    stdout, stderr, rc = run_cmd(
        [
            sys.executable, "-m", "coverage", "run",
            "--source", str(sut_file),
            "-m", "unittest", str(test_file)
        ],
        timeout=60
    )

    # Now get the report only for this file
    stdout_r, stderr_r, rc_r = run_cmd(
        [sys.executable, "-m", "coverage", "report", str(sut_file)],
        timeout=30
    )

    # dbg("--- coverage report ---\n" + stdout_r + "\n------------------------")

    for line in stdout_r.splitlines():
        if "problem_" in line and problem_id in line:
            parts = line.split()
            # last chunk should be like "100%"
            for p in reversed(parts):
                if p.endswith("%"):
                    try:
                        return float(p.replace("%", ""))
                    except Exception:
                        pass

    # If not found, maybe no coverage data
    return 0.0


# ==========================================
# ✅ Passing tests (for mutation)
# ==========================================
def get_passing_tests(problem_id: str):
    test_file = test_file_for(problem_id)
    if not test_file.exists():
        return []

    dbg(f"  [MUT] Getting passing tests via pytest for {test_file}")
    stdout, stderr, rc = run_cmd(
        [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=no"],
        timeout=120
    )

    passing = []
    for line in stdout.splitlines():
        if " PASSED" in line:
            # e.g.: tests_spec/NoSUT_Baseline/problem_HumanEval_0_gen.py::TestFoo::test_x PASSED
            try:
                test_name = line.split("::")[-1].split()[0]
                passing.append(test_name)
            except Exception:
                pass

    dbg(f"    ✔ Passing tests: {passing}")
    return passing


# ==========================================
# ✅ MUTATION (mutmut + results parser)
# ==========================================
def clear_mutmut_cache():
    cache = Path(".mutmut-cache")
    if cache.exists():
        try:
            if cache.is_dir():
                shutil.rmtree(cache)
            else:
                cache.unlink()
        except Exception:
            pass


def calculate_mutation_score(problem_id: str):
    sut_file = sut_file_for(problem_id)
    test_file = test_file_for(problem_id)

    print(f"\n--- MUTATION DEBUG for {problem_id} ---")
    print(f"  SUT:  {sut_file}")
    print(f"  TEST: {test_file}")

    if not sut_file.exists() or not test_file.exists():
        print("  ❌ Missing sut or test, skipping mutation.")
        return None

    passing_tests = get_passing_tests(problem_id)
    if not passing_tests:
        print("  ❌ No passing tests – mutation score = 0.0")
        return 0.0

    selector = " or ".join(passing_tests)
    print(f"  ✔ Using selector: {selector}")

    clear_mutmut_cache()

    # 1) Run mutmut
    cmd = [
        sys.executable, "-m", "mutmut", "run",
        "--paths-to-mutate", str(sut_file),
        "--tests-dir", str(TEST_DIR),
        "--runner",
        f"python -m pytest {test_file} -k '{selector}' --tb=no -q"
    ]
    print("  🔁 Running:", " ".join(map(str, cmd)))

    stdout, stderr, rc = run_cmd(cmd, timeout=300)
    # Uncomment to see raw:
    # print("\n[mutmut stdout]\n", stdout)
    # print("\n[mutmut stderr]\n", stderr)

    # 2) Get summary counts from `mutmut results`
    res_out, res_err, res_rc = run_cmd([sys.executable, "-m", "mutmut", "results"])
    # print("\n[mutmut results]\n", res_out)

    killed = survived = timeout_count = suspicious = 0

    # `mutmut results` prints lines like:
    # "1. killed  (some description)"
    # "2. survived ..."
    for line in res_out.splitlines():
        low = line.strip().lower()
        if not low:
            continue

        if "killed" in low:
            killed += 1
        elif "survived" in low:
            survived += 1
        elif "timeout" in low:
            timeout_count += 1
        elif "suspicious" in low:
            suspicious += 1

    total = killed + survived + timeout_count + suspicious
    print(f"  ➜ Mutants: killed={killed}, survived={survived}, timeout={timeout_count}, suspicious={suspicious}, total={total}")

    if total == 0:
        print("  ⚠️ No mutants found – score=0.0")
        return 0.0

    score = (killed / total) * 100.0
    print(f"  🎯 Mutation score = {score:.2f}%")
    return score


# ==========================================
# 🚀 MAIN
# ==========================================
def main():
    print(f"Starting evaluation using tests from: {TEST_DIR}\n")

    problem_ids = load_problem_ids()
    results = []

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    for idx, pid in enumerate(problem_ids, start=1):
        print(f"\n[{idx}/{len(problem_ids)}] Evaluating {pid}...")

        validity_rate, passing, total = calculate_validity_rate(pid)
        print(f"  Validity Rate: {validity_rate}% ({passing}/{total})")

        coverage = calculate_coverage(pid)
        print(f"  Coverage: {coverage}%")

        mutation_score = calculate_mutation_score(pid)
        print(f"  Mutation Score: {mutation_score}%")

        results.append({
            "problem_id": pid,
            "validity_rate": validity_rate if validity_rate is not None else "N/A",
            "passing_tests": passing,
            "total_tests": total,
            "coverage": coverage if coverage is not None else "N/A",
            "mutation_score": mutation_score if mutation_score is not None else "N/A",
        })

    with OUTPUT_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "problem_id",
                "validity_rate",
                "passing_tests",
                "total_tests",
                "coverage",
                "mutation_score",
            ]
        )
        writer.writeheader()
        writer.writerows(results)

    print("\n==============================================")
    print(f"  Evaluation complete for {TEST_DIR}!")
    print(f"  Results saved to: {OUTPUT_CSV}")
    print("==============================================")


if __name__ == "__main__":
    main()
