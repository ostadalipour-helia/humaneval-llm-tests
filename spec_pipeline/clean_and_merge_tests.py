import os
import re
import sys
import subprocess
from pathlib import Path

###############################
# CONFIG
###############################

BASELINE_DIR = Path("tests")
SPEC_DIR = Path("tests_spec/NoSUT")
OUTPUT_DIR = Path("tests_spec/NoSUT_Baseline")
SUT_DIR = Path("sut")

TEST_FILE_PATTERN = "problem_{id}_gen.py"

DEBUG = True   # turn debug on/off

###############################


def dbg(msg):
    if DEBUG:
        print(msg)


##############################################
#  NEW: CHECK IF OUTPUT ALREADY EXISTS
##############################################
def output_already_exists(problem_id):
    out_file = OUTPUT_DIR / f"problem_{problem_id}_gen.py"
    if not out_file.exists():
        return False

    content = out_file.read_text().strip()
    # If it contains at least one test method, we consider it "done"
    return "def test_" in content


##############################################


def find_spec_file(problem_id):
    """
    Finds matching spec/NoSUT test file using multiple naming conventions.
    """
    candidates = [
        SPEC_DIR / f"problem_{problem_id}_gen.py",
        SPEC_DIR / f"HumanEval_{problem_id}_gen.py",
        SPEC_DIR / f"{problem_id}_gen.py",
    ]

    for c in candidates:
        if c.exists():
            dbg(f"   ✔ Found spec test file: {c}")
            return c

    dbg(f"   ❌ No spec test file found for problem {problem_id}")
    return None


def get_function_name(sut_file):
    text = sut_file.read_text()
    m = re.search(r"def\s+(\w+)\s*\(", text)
    if not m:
        raise ValueError(f"❌ Could not find function name in {sut_file}")
    func = m.group(1)
    dbg(f"   ➤ Detected function name: {func}")
    return func


def extract_test_functions(test_file):
    if test_file is None or not test_file.exists():
        dbg(f"   ❌ Test file not found: {test_file}")
        return []

    dbg(f"   ✔ Reading tests from: {test_file}")
    text = test_file.read_text()

    dbg("   File head:\n" + text[:200].replace("\n", "\\n") + "\n---")

    tests = re.split(r'\n\s*def ', text)[1:]
    dbg(f"   ➤ Extracted {len(tests)} raw test blocks")

    result = []
    for t in tests:
        name = t.split("(")[0]
        full = "def " + t
        result.append((name.strip(), full))

    dbg(f"   ➤ Parsed {len(result)} test functions\n")
    return result


def run_single_test(problem_id, function_name, test_function_text):
    TEMP = Path("temp_single_test.py")

    patched_text = test_function_text.replace(f"{function_name}(", f"mod.{function_name}(")

    wrapper = (
        "import unittest\n"
        f"import sut.problem_{problem_id} as mod\n\n"
        "class TempTest(unittest.TestCase):\n"
        + "\n".join("    " + line for line in patched_text.split("\n"))
        + "\n\nif __name__ == '__main__':\n"
        "    unittest.main()\n"
    )

    TEMP.write_text(wrapper)

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "temp_single_test.py", "-q", "--tb=no"],
            capture_output=True,
            text=True,
            timeout=5   # <── timeout added
        )
    except subprocess.TimeoutExpired:
        dbg("   ⏳ TIMEOUT — test hung, dropping.")
        TEMP.unlink(missing_ok=True)
        return False

    TEMP.unlink(missing_ok=True)
    return "1 passed" in result.stdout.lower()



def clean_and_merge(problem_id):
    ##############################################
    # NEW LOGIC: SKIP WHEN OUTPUT ALREADY EXISTS
    ##############################################
    if output_already_exists(problem_id):
        print(f"⏩ Skipping {problem_id} (already generated)")
        return
    ##############################################

    dbg("\n==============================")
    dbg(f" CLEANING PROBLEM {problem_id}")
    dbg("==============================\n")

    sut_file = sut_file_for(problem_id)
    function_name = get_function_name(sut_file)

    baseline_file = BASELINE_DIR / TEST_FILE_PATTERN.format(id=problem_id)
    spec_file = find_spec_file(problem_id)

    baseline_tests = extract_test_functions(baseline_file)
    spec_tests = extract_test_functions(spec_file)

    dbg(f">>> TOTAL baseline tests: {len(baseline_tests)}")
    dbg(f">>> TOTAL spec tests: {len(spec_tests)}")

    kept_tests = []
    seen_norm = set()

    def normalize(name):
        return re.sub(r"_again|_second_time|_third_time", "", name.lower())

    # baseline
    for name, text in baseline_tests:
        dbg(f"\n▶ Testing BASELINE: {name}")
        if run_single_test(problem_id, function_name, text):
            n = normalize(name)
            if n not in seen_norm:
                kept_tests.append((name, text))
                seen_norm.add(n)
                dbg(f"   ✔ Keeping baseline test")
        else:
            dbg(f"   ✖ Dropped baseline test")

    # spec
    for name, text in spec_tests:
        dbg(f"\n▶ Testing SPEC: {name}")
        if run_single_test(problem_id, function_name, text):
            n = normalize(name)
            if n not in seen_norm:
                kept_tests.append((name, text))
                seen_norm.add(n)
                dbg(f"   ✔ Keeping spec test")
        else:
            dbg(f"   ✖ Dropped spec test")

    write_clean_hybrid(problem_id, function_name, kept_tests)


def sut_file_for(problem_id):
    return SUT_DIR / f"problem_{problem_id}.py"


def write_clean_hybrid(problem_id, function_name, tests):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUTPUT_DIR / f"problem_{problem_id}_gen.py"

    header = (
        "import unittest\n"
        f"import sut.problem_{problem_id} as mod\n\n"
        "class TestHybrid(unittest.TestCase):\n"
    )

    body = ""
    for _, text in tests:
        method = "\n".join("    " + l for l in text.split("\n"))
        method = method.replace(f"{function_name}(", f"mod.{function_name}(")
        body += method + "\n\n"

    dbg(f"Writing {len(tests)} tests → {out_file}")
    out_file.write_text(header + body)


def main():
    problem_ids = sorted([
        p.stem.replace("problem_", "") for p in SUT_DIR.glob("problem_*.py")
    ])

    for pid in problem_ids:
        clean_and_merge(pid)

    print("\n🔥 Hybrid cleaning complete! Output:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
