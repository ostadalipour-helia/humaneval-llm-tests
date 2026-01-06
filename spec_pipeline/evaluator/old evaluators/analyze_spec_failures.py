import pandas as pd

baseline = pd.read_csv("results/metrics.csv")
spec     = pd.read_csv("results/metrics_spec.csv")

merged = baseline.merge(spec, on="problem_id", suffixes=("_base", "_spec"))

merged["validity_diff"] = merged["validity_rate_spec"] - merged["validity_rate_base"]

# Measure spec-induced failure rate
spec_harmed = (merged["validity_diff"] < 0).sum()
spec_helped = (merged["validity_diff"] > 0).sum()
spec_neutral = (merged["validity_diff"] == 0).sum()

print("\nSPEC ERROR ANALYSIS")
print("====================")
print(f"Spec helped:        {spec_helped}")
print(f"Spec harmed:        {spec_harmed}")
print(f"No change:          {spec_neutral}")

print(f"\nSpec harm rate:     {spec_harmed / len(merged) * 100:.2f}%")
print(f"Spec help rate:     {spec_helped / len(merged) * 100:.2f}%")
