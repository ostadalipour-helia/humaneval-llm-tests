#!/usr/bin/env python3
"""
Unified evaluator for:
- baseline
- spec_NoSUT
- spec_SUT
- hybrid (NoSUT_Baseline)

Produces CSVs:
    result_spec/metrics_baseline.csv
    result_spec/metrics_spec_NoSUT.csv
    result_spec/metrics_spec_SUT.csv
    result_spec/metrics_hybrid.csv

IMPROVEMENTS:
1. Added timeout mechanism to prevent hanging on problematic tests
2. Better handling of partial test failures in mutation testing
3. Option to run mutation testing only on passing test methods
"""

import csv
import subprocess
import sys
import gzip
import json
from pathlib import Path
import shutil
import re
import ast
import signal

# ============================================================
# SETTINGS
# ============================================================
ROOT = Path(__file__).resolve().parents[2]
DEBUG = False  # turn on/off all debug printing
MUTATION_TIMEOUT = 60  # 5 minutes per problem
USE_PASSING_TESTS_ONLY = True  # Only run mutation on passing tests


def dbg(msg):
    if DEBUG:
        print(msg)


# ============================================================
# DIRECTORIES
# ============================================================
SUT_DIR = ROOT / "sut"
DATA_PATH = ROOT / "humaneval" / "data" / "HumanEval.jsonl.gz"

TEST_SUITES = {
    "baseline": ROOT / "tests",
    "spec_NoSUT": ROOT / "tests_spec" / "NoSUT",
    "spec_SUT": ROOT / "tests_spec" / "SUT",
    "hybrid": ROOT / "tests_spec" / "NoSUT_Baseline",
}

OUTPUT_DIR = ROOT / "result_spec"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# LOAD ALL PROBLEM IDS
# ============================================================
def load_problem_ids():
    pids = []
    with gzip.open(DATA_PATH, "rt", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            pids.append(obj["task_id"].replace("/", "_"))
    return pids


# ============================================================
# FILE LOCATORS
# ============================================================
def locate_test_file(suite_dir, pid):
    num = pid.split("_")[-1]

    patterns = [
        f"problem_{pid}_gen.py",
        f"{pid}_gen.py",
        f"*{pid}_gen.py",
        f"HumanEval_{num}_gen.py",
        f"*{num}_gen.py",
    ]

    for pat in patterns:
        matches = list(suite_dir.glob(pat))
        if matches:
            dbg(f"  ✔ Found test file via pattern '{pat}': {matches[0]}")
            return matches[0]

    dbg(f"  ❌ No test file found for PID={pid}")
    return None


def locate_sut_file(pid):
    num = pid.split("_")[-1]

    patterns = [
        f"problem_{pid}.py",
        f"{pid}.py",
        f"problem_HumanEval_{num}.py",
        f"*{pid}.py",
        f"*{num}.py",
    ]

    for pat in patterns:
        matches = list(SUT_DIR.glob(pat))
        if matches:
            dbg(f"  ✔ Found SUT file via pattern '{pat}': {matches[0]}")
            return matches[0]

    dbg(f"  ❌ No SUT file found for PID={pid}")
    return None


# ============================================================
# GET PASSING TEST METHODS
# ============================================================
def get_passing_test_methods(test_file):
    """
    Run tests and identify which specific test methods are passing.
    Returns a list of test method names (e.g., ['test_example_1', 'test_example_2'])
    """
    if not test_file or not test_file.exists():
        return []
    
    dbg(f"  [PASSING TESTS] Identifying passing tests in {test_file.name}")
    
    try:
        # Run pytest with verbose output to see individual test results
        proc = subprocess.run(
            [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=no"],
            capture_output=True, text=True, timeout=60
        )
        
        output = proc.stdout + proc.stderr
        dbg(f"  pytest output:\n{output}")
        
    except subprocess.TimeoutExpired:
        print(f"  ⚠️ Test identification timed out after 60 seconds for {test_file.name}")
        dbg(f"  [PASSING TESTS] Timeout occurred, returning empty list")
        return []
    
    passing_tests = []
    
    # Parse output for PASSED tests
    # Format: "test_file.py::TestClass::test_method PASSED"
    for line in output.splitlines():
        if "PASSED" in line and "::" in line:
            # Extract test method name
            parts = line.split("::")
            if len(parts) >= 2:
                test_name = parts[-1].split()[0]  # Get method name before PASSED
                passing_tests.append(test_name)
                dbg(f"    ✔ Found passing test: {test_name}")
    
    return passing_tests


# ============================================================
# CREATE FILTERED TEST FILE
# ============================================================
def create_filtered_test_file(original_test_file, passing_tests, temp_dir):
    """
    Create a temporary test file containing only the passing test methods.
    """
    if not passing_tests:
        return None
    
    temp_file = temp_dir / original_test_file.name
    
    with open(original_test_file, 'r') as f:
        content = f.read()
    
    # Parse the AST to extract only passing test methods
    try:
        tree = ast.parse(content)
        
        # Find all test classes
        new_body = []
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                # Filter methods to keep only passing ones
                filtered_methods = []
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        if item.name in passing_tests or not item.name.startswith('test_'):
                            filtered_methods.append(item)
                
                if filtered_methods:
                    node.body = filtered_methods
                    new_body.append(node)
            else:
                # Keep imports and other top-level code
                new_body.append(node)
        
        tree.body = new_body
        
        # Write the filtered content
        filtered_content = ast.unparse(tree)
        with open(temp_file, 'w') as f:
            f.write(filtered_content)
        
        dbg(f"  ✔ Created filtered test file with {len(passing_tests)} passing tests")
        return temp_file
        
    except Exception as e:
        dbg(f"  ❌ Failed to create filtered test file: {e}")
        return None


# ============================================================
# VALIDITY
# ============================================================
def get_validity(test_file):
    if not test_file or not test_file.exists():
        dbg("  [VALIDITY] Missing file → None")
        return None, 0, 0

    dbg(f"  [VALIDITY] Running unittest on {test_file.name}")
    
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "unittest", str(test_file)],
            capture_output=True, text=True, timeout=60
        )
    except subprocess.TimeoutExpired:
        dbg("  [VALIDITY] Test execution timed out")
        return None, 0, 0

    output = proc.stdout + proc.stderr
    dbg("  unittest OUTPUT:\n" + output)

    if "Ran " not in output:
        return None, 0, 0

    try:
        total = int(output.split("Ran ")[1].split()[0])
    except:
        return None, 0, 0

    failed = output.count("FAIL") + output.count("ERROR")
    passing = total - failed
    rate = 100 * passing / total if total else None
    return rate, passing, total


# ============================================================
# COVERAGE
# ============================================================
def get_coverage(pid, test_file):
    sut_file = locate_sut_file(pid)
    if not sut_file or not test_file:
        return None

    dbg(f"  [COVERAGE] Running coverage for {pid}")

    try:
        subprocess.run([sys.executable, "-m", "coverage", "erase"], timeout=10)

        subprocess.run([
            sys.executable, "-m", "coverage", "run",
            "--source=sut",
            "-m", "unittest", str(test_file)
        ], capture_output=True, text=True, timeout=60)

        report = subprocess.run(
            [sys.executable, "-m", "coverage", "report"],
            capture_output=True, text=True, timeout=10
        )
    except subprocess.TimeoutExpired:
        dbg("  [COVERAGE] Coverage execution timed out")
        return None

    dbg("  coverage OUTPUT:\n" + report.stdout)

    for line in report.stdout.splitlines():
        if f"problem_{pid}" in line:
            try:
                return float(line.split()[-1].replace("%", ""))
            except:
                return None

    return None


# ============================================================
# MUTATION — IMPROVED WITH TIMEOUT AND PARTIAL TEST HANDLING
# ============================================================
def clear_mutmut_cache():
    cache = Path(".mutmut-cache")
    if cache.exists():
        shutil.rmtree(cache, ignore_errors=True)


def extract_safe_int(s):
    """Return the first integer found in a string, or None."""
    matches = re.findall(r'\d+', s)
    if matches:
        try:
            return int(matches[0])
        except:
            return None
    return None


def parse_mutmut_summary(summary_line, debug=False):
    """Parse a single mutmut summary line like:
    '⠹ 6/6  🎉 6  ⏰ 0  🤔 0  🙁 0  🔇 0'
    """
    if debug or DEBUG:
        print(f"\n🔍 PARSING SUMMARY LINE:\n{repr(summary_line)}\n")
    
    killed = survived = timeout = suspicious = skipped = 0

    if "🎉" in summary_line:
        parts = summary_line.split("🎉")
        if len(parts) > 1:
            v = extract_safe_int(parts[1])
            if v is not None:
                killed = v

    if "🙁" in summary_line:
        parts = summary_line.split("🙁")
        if len(parts) > 1:
            v = extract_safe_int(parts[1])
            if v is not None:
                survived = v

    if "⏰" in summary_line:
        parts = summary_line.split("⏰")
        if len(parts) > 1:
            v = extract_safe_int(parts[1])
            if v is not None:
                timeout = v

    if "🤔" in summary_line:
        parts = summary_line.split("🤔")
        if len(parts) > 1:
            v = extract_safe_int(parts[1])
            if v is not None:
                suspicious = v

    if "🔇" in summary_line:
        parts = summary_line.split("🔇")
        if len(parts) > 1:
            v = extract_safe_int(parts[1])
            if v is not None:
                skipped = v

    total = killed + survived + timeout + suspicious + skipped
    
    if debug or DEBUG:
        print(f"  Parsed: killed={killed}, survived={survived}, timeout={timeout}, suspicious={suspicious}, skipped={skipped}, total={total}")

    if total == 0:
        return None

    return 100 * killed / total


def get_mutation(pid, test_file, suite_dir, debug=False):
    """Mutation testing with timeout and support for partial test failures."""
    sut_file = locate_sut_file(pid)
    if not sut_file or not test_file:
        return None

    # Clean cache
    cache = Path(".mutmut-cache")
    if cache.exists():
        try:
            if cache.is_file():
                cache.unlink()
            else:
                shutil.rmtree(cache)
        except:
            pass

    # -------------------------
    # OPTIONAL: Use only passing tests
    # -------------------------
    actual_test_file = test_file
    temp_dir = None
    
    if USE_PASSING_TESTS_ONLY:
        passing_tests = get_passing_test_methods(test_file)
        
        if passing_tests:
            dbg(f"  Found {len(passing_tests)} passing tests, creating filtered test file")
            temp_dir = Path("/tmp") / f"mutmut_temp_{pid}"
            temp_dir.mkdir(exist_ok=True, parents=True)
            
            filtered_file = create_filtered_test_file(test_file, passing_tests, temp_dir)
            if filtered_file:
                actual_test_file = filtered_file
        else:
            print(f"  ⚠️ No passing tests found for {pid} (may have timed out), skipping mutation testing")
            return 0.0

    # -------------------------
    # 1. RUN mutmut run with timeout
    # -------------------------
    cmd = [
        sys.executable, "-m", "mutmut", "run",
        "--paths-to-mutate", str(sut_file),
        "--runner", f"python -m pytest {actual_test_file} --tb=no -q"
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=MUTATION_TIMEOUT)
        raw = proc.stdout + proc.stderr
    except subprocess.TimeoutExpired:
        if debug or DEBUG:
            print(f"⚠️ Mutation testing timed out for {pid}")
        
        # Clean up temp directory
        if temp_dir and temp_dir.exists():
            shutil.rmtree(temp_dir, ignore_errors=True)
        
        return None

    if debug:
        print("\n📜 RAW MUTMUT RUN OUTPUT:\n")
        print(raw)

    # Clean up temp directory
    if temp_dir and temp_dir.exists():
        shutil.rmtree(temp_dir, ignore_errors=True)

    # -------------------------
    # Try to parse summary line
    # -------------------------
    summary_lines = [
        line for line in raw.splitlines()
        if "🎉" in line and "/" in line
    ]

    if summary_lines:
        return parse_mutmut_summary(summary_lines[-1], debug)

    # -------------------------
    # BASELINE FAILED → FALLBACK TO `mutmut results`
    # -------------------------
    if debug or DEBUG:
        print("⚠️ No summary found — baseline failure. Using mutmut results fallback.\n")

    try:
        proc2 = subprocess.run(
            [sys.executable, "-m", "mutmut", "results"],
            capture_output=True, text=True, timeout=30
        )
    except subprocess.TimeoutExpired:
        if debug or DEBUG:
            print("⚠️ mutmut results timed out")
        return None

    results_raw = proc2.stdout + proc2.stderr

    if debug or DEBUG:
        print("\n📜 RAW mutmut results OUTPUT:\n")
        print(results_raw)
        print("\n")

    # Check if mutmut results crashed
    if "Traceback" in results_raw or "IndexError" in results_raw:
        if debug or DEBUG:
            print("⚠️ mutmut results crashed. Reading .mutmut-cache database directly.\n")
        
        cache_file = Path(".mutmut-cache")
        if cache_file.exists():
            try:
                import sqlite3
                conn = sqlite3.connect(str(cache_file))
                cursor = conn.cursor()
                
                cursor.execute("SELECT status, COUNT(*) FROM Mutant GROUP BY status")
                results = cursor.fetchall()
                
                if debug or DEBUG:
                    print(f"  Raw status counts: {results}\n")
                
                conn.close()
                
                status_map = {
                    'killed': 0,
                    'survived': 0, 
                    'timeout': 0,
                    'suspicious': 0,
                    'skipped': 0
                }
                
                for status, count in results:
                    status_str = str(status).lower()
                    if debug or DEBUG:
                        print(f"  Processing status: {status} (count={count})")
                    
                    if 'kill' in status_str or status == 'ok_killed':
                        status_map['killed'] += count
                    elif 'surviv' in status_str or status == 'bad_survived':
                        status_map['survived'] += count
                    elif 'timeout' in status_str or status == 'bad_timeout':
                        status_map['timeout'] += count
                    elif 'suspicious' in status_str or status == 'ok_suspicious':
                        status_map['suspicious'] += count
                    elif 'skip' in status_str or status == 'skipped':
                        status_map['skipped'] += count
                
                killed = status_map['killed']
                survived = status_map['survived']
                timeout = status_map['timeout']
                suspicious = status_map['suspicious']
                skipped = status_map['skipped']
                
                total_tested = killed + survived + timeout + suspicious
                
                if debug or DEBUG:
                    print(f"  Parsed from cache DB: killed={killed}, survived={survived}, timeout={timeout}, suspicious={suspicious}, skipped={skipped}")
                    print(f"  Total tested: {total_tested}\n")
                
                if total_tested == 0:
                    return 0.0
                
                return 100 * killed / total_tested
                
            except Exception as e:
                if debug or DEBUG:
                    print(f"  Failed to read cache: {e}\n")
                return 0.0
        else:
            if debug or DEBUG:
                print("  No .mutmut-cache file found.\n")
            return 0.0

    # Parse results output
    killed = survived = timeout = suspicious = skipped = 0

    for line in results_raw.splitlines():
        val = extract_safe_int(line)
        if val is None:
            continue

        if debug or DEBUG:
            print(f"  Processing line: {repr(line)} -> val={val}")

        if "🎉" in line:
            killed += val
        elif "🙁" in line:
            survived += val
        elif "⏰" in line:
            timeout += val
        elif "🤔" in line:
            suspicious += val
        elif "🔇" in line:
            skipped += val

    total_tested = killed + survived + timeout + suspicious

    if debug or DEBUG:
        print(f"\n  FALLBACK TOTALS: killed={killed}, survived={survived}, timeout={timeout}, suspicious={suspicious}, skipped={skipped}")
        print(f"  Total tested: {total_tested}\n")

    if total_tested == 0:
        return 0.0

    return 100 * killed / total_tested


# ============================================================
# SUITE EVALUATION
# ============================================================
def evaluate_suite(name, suite_dir):
    print(f"\n==============================")
    print(f" Evaluating suite: {name}")
    print(f"==============================\n")

    pids = load_problem_ids()
    rows = []
    out_csv = OUTPUT_DIR / f"metrics_{name}.csv"

    for i, pid in enumerate(pids, 1):
        print(f"\n→ [{i}/{len(pids)}] {pid}")

        test_file = locate_test_file(suite_dir, pid)
        sut_file = locate_sut_file(pid)

        validity, passing, total = get_validity(test_file)
        coverage = get_coverage(pid, test_file)
        mutation = get_mutation(pid, test_file, suite_dir)

        print(f"  ✔ VALIDITY: {validity}% ({passing}/{total} passing)")
        print(f"  ✔ COVERAGE: {coverage}%")
        print(f"  ✔ MUTATION: {mutation}%")

        rows.append({
            "problem_id": pid,
            "validity_rate": validity,
            "passing_tests": passing,
            "total_tests": total,
            "coverage": coverage,
            "mutation_score": mutation,
        })
        
        # Save progress after each problem
        with open(out_csv, "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "problem_id", "validity_rate", "passing_tests",
                    "total_tests", "coverage", "mutation_score"
                ]
            )
            writer.writeheader()
            writer.writerows(rows)

    print(f"\n📄 Saved → {out_csv}")


# ============================================================
# MAIN
# ============================================================
def main():
    print(f"\n🔧 Configuration:")
    print(f"   - Mutation timeout: {MUTATION_TIMEOUT}s")
    print(f"   - Use passing tests only: {USE_PASSING_TESTS_ONLY}")
    print(f"   - Debug mode: {DEBUG}\n")
    
    for name, folder in TEST_SUITES.items():
        evaluate_suite(name, folder)

    print("\n🎉 DONE — all suites evaluated!\n")


if __name__ == "__main__":
    main()
