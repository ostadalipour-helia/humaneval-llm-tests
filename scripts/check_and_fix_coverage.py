# check_and_fix_coverage.py
import ast
from pathlib import Path

SUT_DIR = Path("sut_llm")

def find_broken_files():
    """Find all files with syntax errors."""
    broken = []
    for py_file in sorted(SUT_DIR.glob("problem_*.py")):
        try:
            with open(py_file, 'r') as f:
                ast.parse(f.read())
        except SyntaxError:
            broken.append(py_file.name)
    return broken

if __name__ == "__main__":
    broken = find_broken_files()
    if broken:
        print(f"Found {len(broken)} files with syntax errors:")
        for f in broken:
            print(f"  - {f}")
        
        # Create a coverage config file
        with open(".coveragerc", "w") as f:
            f.write("[run]\n")
            f.write("source = sut_llm\n")
            f.write("omit = \n")
            for broken_file in broken:
                f.write(f"    sut_llm/{broken_file}\n")
        
        print(f"\n✅ Created .coveragerc to exclude these files")
    else:
        print("No syntax errors found!")