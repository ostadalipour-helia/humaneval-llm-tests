import subprocess
import sys
from pathlib import Path
import json
import coverage

def debug_one(problem_id):
    print("\n==============================")
    print(f"🔍 DEEP DEBUG FOR: {problem_id}")
    print("==============================\n")

    sut = Path(f"sut/problem_{problem_id}.py")
    test = Path(f"tests_spec/NoSUT_Baseline/problem_{problem_id}_gen.py")

    # Check existence
    print(sut)
    print(test)
    print("📁 FILE CHECK")
    print("SUT exists?  ", sut.exists())
    print("TEST exists? ", test.exists())
    print()

    if test.exists():
        print("📄 TEST FILE CONTENTS")
        print(test.read_text())
        print("\n-------------------------------------\n")
    else:
        print("❌ Test file missing!")
        return

    if sut.exists():
        print("📄 SUT FILE CONTENTS")
        print(sut.read_text())
        print("\n-------------------------------------\n")
    else:
        print("❌ SUT file missing!")
        return

    # ============ VALIDITY TEST ============
    print("\n🧪 VALIDITY TEST (unittest)")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "unittest", str(test)],
            capture_output=True,
            text=True,
            timeout=30
        )
        print(result.stdout)
        print(result.stderr)

        # extract numbers
        total = None
        for line in (result.stdout + result.stderr).splitlines():
            if "Ran " in line:
                total = int(line.split()[1])
                break

        failed = (result.stdout + result.stderr).count("FAIL") + \
                 (result.stdout + result.stderr).count("ERROR")

        if total is not None:
            print(f"✔ TOTAL TESTS:   {total}")
            print(f"✔ FAILURES:      {failed}")
            print(f"✔ VALIDITY RATE: {(1 - failed/total)*100:.2f}%")

    except Exception as e:
        print("❌ ERROR:", e)

    # ============ COVERAGE TEST ============
    print("\n📊 COVERAGE TEST")
    try:
        subprocess.run(
            ["coverage", "run", "--source=sut", "-m", "unittest", str(test)],
            text=True,
            capture_output=True
        )

        report = subprocess.run(
            ["coverage", "report"],
            capture_output=True,
            text=True
        )

        print(report.stdout)

        # Parse sut file line
        for line in report.stdout.splitlines():
            if f"problem_{problem_id}" in line:
                cov = float(line.split()[-1].replace("%", ""))
                print(f"✔ COVERAGE: {cov}%")
                break

    except Exception as e:
        print("❌ COVERAGE ERROR:", e)

    # ============ MUTATION TEST ============
    print("\n💥 MUTATION TEST (mutmut)")
    try:
        # Clean cache
        cache = Path(".mutmut-cache")
        if cache.exists():
            if cache.is_file(): cache.unlink()
            else:
                import shutil
                shutil.rmtree(cache)

        result = subprocess.run(
            [
                sys.executable, "-m", "mutmut", "run",
                "--paths-to-mutate", f"sut/problem_{problem_id}.py",
                "--tests-dir", "tests_spec/",
                "--runner", f"python -m pytest {test} -q --tb=no"
            ],
            capture_output=True,
            text=True,
            timeout=180
        )

        print(result.stdout)
        print(result.stderr)

        # Extract counts
        killed = survived = timeouts = suspicious = 0

        for line in result.stdout.splitlines():
            if "🎉" in line:  # killed
                killed = int(line.split()[1])
            if "🙁" in line:  # survived
                survived = int(line.split()[1])
            if "⏰" in line:  # timeout
                timeouts = int(line.split()[1])
            if "🤔" in line:  # suspicious
                suspicious = int(line.split()[1])

        total = killed + survived + timeouts + suspicious
        print(f"\n✔ MUTANTS TOTAL:     {total}")
        print(f"✔ KILLED:            {killed}")
        print(f"✔ SURVIVED:          {survived}")
        print(f"✔ TIMEOUT:           {timeouts}")
        print(f"✔ SUSPICIOUS:        {suspicious}")

        if total > 0:
            print(f"✔ MUTATION SCORE:    {killed/total*100:.2f}%")

    except Exception as e:
        print("❌ MUTATION ERROR:", e)

    print("\n==============================")
    print("      DEBUG COMPLETE")
    print("==============================\n")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python debug_one_problem.py HumanEval_86")
    else:
        debug_one(sys.argv[1])
