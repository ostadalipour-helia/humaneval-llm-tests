import ast
import pandas as pd
from pathlib import Path
import re

TEST_DIR = Path("tests_spec")

def extract_inputs(test_file):
    """Extract inputs from assertEqual(f(...), ...) patterns."""
    text = test_file.read_text()
    calls = re.findall(rf"{re.escape('(')}(.*?){re.escape(')')}", text)
    # Returns argument strings – usable for basic diversity metrics
    return calls

def main():
    all_inputs = []

    for f in TEST_DIR.glob("*.py"):
        inputs = extract_inputs(f)
        all_inputs.extend(inputs)

    # Diversity metrics
    total = len(all_inputs)
    unique = len(set(all_inputs))

    print("\n📘 Edge-case Diversity")
    print(f"Total test inputs: {total}")
    print(f"Unique test inputs: {unique}")
    print(f"Diversity ratio: {unique / total * 100:.2f}%")

if __name__ == "__main__":
    main()
