import gzip
import json
from pathlib import Path

DATA_PATH = Path("data/humaneval/data/HumanEval.jsonl.gz")
OUT_DIR = Path("sut")
OUT_DIR.mkdir(parents=True, exist_ok=True)

with gzip.open(DATA_PATH, "rt", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        task_id = obj["task_id"].replace("/", "_")   # e.g., HumanEval_0
        
        # Get the prompt (contains function signature) and solution
        prompt = obj["prompt"]  # This has the function header!
        solution_code = obj["canonical_solution"]
        
        # Combine prompt + solution to get complete function
        complete_code = prompt + solution_code
        
        # Write to sut/problem_<id>.py
        out_file = OUT_DIR / f"problem_{task_id}.py"
        with open(out_file, "w") as fw:
            fw.write(complete_code + "\n")
        
        print(f"Wrote {out_file}")

print(f"\nGenerated {len(list(OUT_DIR.glob('*.py')))} SUT files")
