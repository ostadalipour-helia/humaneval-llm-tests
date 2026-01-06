#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2]
SUT_DIR = ROOT / "sut"
TEST_DIR = ROOT / "tests_spec" / "NoSUT"       # or switch to spec_NoSUT etc.

def locate_sut(pid):
    num = pid.split("_")[-1]
    patterns = [
        f"problem_{pid}.py",
        f"problem_HumanEval_{num}.py",
        f"*{num}.py",
    ]
    for pat in patterns:
        m = list(SUT_DIR.glob(pat))
        if m:
            return m[0]
    return None

def locate_test(pid):
    num = pid.split("_")[-1]
    patterns = [
        f"problem_{pid}_gen.py",
        f"HumanEval_{num}_gen.py",
        f"*{num}_gen.py",
    ]
    for pat in patterns:
        m = list(TEST_DIR.glob(pat))
        if m:
            return m[0]
    return None

def clear_cache():
    cache = Path(".mutmut-cache")
    if cache.exists():
        if cache.is_file():
            cache.unlink()
        else:
            shutil.rmtree(cache, ignore_errors=True)

def parse_summary(raw):
    lines = raw.splitlines()
    summary = [l for l in lines if "🎉" in l and "/" in l]
    if not summary:
        print("❌ No final summary found.")
        return None

    final = summary[-1]
    print("🔎 SUMMARY LINE:", final)

    tokens = final.replace("/", " ").split()
    killed = survived = suspicious = timeout = skipped = 0

    for i,t in enumerate(tokens):
        if t == "🎉":
            killed = int(tokens[i+1])
        elif t == "🙁":
            survived = int(tokens[i+1])
        elif t == "🤔":
            suspicious = int(tokens[i+1])
        elif t == "⏰":
            timeout = int(tokens[i+1])
        elif t == "🔇":
            skipped = int(tokens[i+1])

    total = killed + survived + suspicious + timeout + skipped
    if total == 0:
        print("⚠️ TOTAL=0 → something failed.")
        return None

    score = 100 * killed / total
    print(f"\n📌 PARSED:")
    print(f"  killed={killed}")
    print(f"  survived={survived}")
    print(f"  suspended={suspicious}")
    print(f"  timeout={timeout}")
    print(f"  skipped={skipped}")
    print(f"  total={total}")
    print(f"  score={score:.2f}")
    return score

def run_one(pid):
    sut = locate_sut(pid)
    test = locate_test(pid)

    if not sut:
        print("❌ No SUT found")
        return
    if not test:
        print("❌ No test file found")
        return

    print(f"\n=== MUTATION TESTING {pid} ===")
    print("SUT:", sut)
    print("TEST:", test)

    clear_cache()

    cmd = [
        sys.executable, "-m", "mutmut", "run",
        "--paths-to-mutate", str(sut),
        "--runner", f"python -m pytest {test} --tb=no -q"
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    raw = proc.stdout + proc.stderr

    print("\n📜 RAW OUTPUT:\n", raw)
    parse_summary(raw)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 debug_mutation_single.py HumanEval_0")
        sys.exit(1)
    run_one(sys.argv[1])
