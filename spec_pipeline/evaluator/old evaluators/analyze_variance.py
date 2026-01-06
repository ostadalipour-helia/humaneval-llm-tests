import pandas as pd
from pathlib import Path
import statistics

BASE = Path("results/metrics.csv")
SPEC = Path("results/metrics_spec.csv")
CMP  = Path("results/metrics_comparison.csv")

def safe_float(x):
    try:
        return float(x)
    except:
        return None

def load_mutations(path):
    df = pd.read_csv(path)
    df["mutation_score"] = df["mutation_score"].apply(safe_float)
    return df["mutation_score"].dropna().tolist()

def main():
    print("\n📊 VARIANCE ANALYSIS\n")

    base_scores = load_mutations(BASE)
    spec_scores = load_mutations(SPEC)

    print(f"Baseline mutation mean:     {statistics.mean(base_scores):.2f}")
    print(f"Baseline mutation stdev:    {statistics.stdev(base_scores):.2f}")

    print(f"Spec mutation mean:         {statistics.mean(spec_scores):.2f}")
    print(f"Spec mutation stdev:        {statistics.stdev(spec_scores):.2f}")

    improvement = statistics.mean(spec_scores) - statistics.mean(base_scores)
    print(f"\nAverage mutation improvement: {improvement:.2f}")

    variance_change = statistics.stdev(spec_scores) - statistics.stdev(base_scores)
    print(f"Variance change:              {variance_change:.2f}")

    print("\nInterpretation:")
    if variance_change < 0:
        print("✔ Spec pipeline REDUCED variance.")
    else:
        print("❌ Spec pipeline INCREASED variance.")

    print()

if __name__ == "__main__":
    main()
