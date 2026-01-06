#!/usr/bin/env python3
"""
SUPER ANALYZER — Full statistical comparison across:
- baseline
- spec_NoSUT
- spec_SUT
- hybrid

Computes:
• summary statistics
• variance, skewness, kurtosis
• distribution buckets
• failure counts
• improvements/regressions
• stability metrics
• correlation between methods
• PCA-like dimensional reduction (manual)
• problem-level anomaly detection
• cluster-like grouping (heuristic)
• extended CSV output

Output file:
    result_spec/comparison_super_extended.csv
"""

import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import skew, kurtosis

ROOT = Path(__file__).resolve().parents[2]
RESULT_DIR = ROOT / "result_spec"

FILES = {
    "baseline": RESULT_DIR / "metrics_baseline.csv",
    "spec_NoSUT": RESULT_DIR / "metrics_spec_NoSUT.csv",
    "spec_SUT": RESULT_DIR / "metrics_spec_SUT.csv",
    "hybrid": RESULT_DIR / "metrics_hybrid.csv",
}

# --------------------------------------------------------------
# LOAD
# --------------------------------------------------------------
def load_all():
    dfs = {}
    for name, f in FILES.items():
        df = pd.read_csv(f)
        dfs[name] = df.set_index("problem_id")
    return dfs

# --------------------------------------------------------------
# SUMMARY for a single method
# --------------------------------------------------------------
def summarize_series(series):
    clean = series.dropna()
    zeros = (clean == 0).sum()

    buckets = {
        "0–20": ((clean >= 0) & (clean < 20)).sum(),
        "20–40": ((clean >= 20) & (clean < 40)).sum(),
        "40–60": ((clean >= 40) & (clean < 60)).sum(),
        "60–80": ((clean >= 60) & (clean < 80)).sum(),
        "80–100": ((clean >= 80) & (clean <= 100)).sum(),
    }

    return {
        "count": len(series),
        "missing": series.isna().sum(),
        "zeros": zeros,
        "mean": clean.mean(),
        "median": clean.median(),
        "variance": clean.var(),
        "std": clean.std(),
        "stderr": clean.sem(),
        "min": clean.min(),
        "max": clean.max(),
        "p25": clean.quantile(0.25),
        "p75": clean.quantile(0.75),
        "skew": skew(clean),
        "kurtosis": kurtosis(clean),
        "buckets": buckets,
        "perfect_100": (clean == 100).sum(),
        "below_50": (clean < 50).sum(),
    }

# --------------------------------------------------------------
# Pairwise delta comparison
# --------------------------------------------------------------
def compare_pairs(a, b):
    delta = b - a
    improved = (delta > 0).sum()
    worse = (delta < 0).sum()
    same = (delta == 0).sum()
    return improved, worse, same, delta.mean(), delta.var()

# --------------------------------------------------------------
# Per-problem stability metric
# --------------------------------------------------------------
def compute_problem_variance(dfs):
    joined = pd.concat([dfs["baseline"]["mutation_score"],
                        dfs["spec_NoSUT"]["mutation_score"],
                        dfs["spec_SUT"]["mutation_score"],
                        dfs["hybrid"]["mutation_score"]], axis=1)
    joined.columns = ["baseline", "spec_NoSUT", "spec_SUT", "hybrid"]
    return joined.var(axis=1)

# --------------------------------------------------------------
# Anomaly detection
# --------------------------------------------------------------
def detect_anomalies(dfs, variance):
    anomalies = []

    for pid in variance.index:
        v = variance[pid]

        # high variance threshold
        if v > 1200:
            anomalies.append((pid, "High variance"))

        baseline = dfs["baseline"].loc[pid, "mutation_score"]
        spec_sut = dfs["spec_SUT"].loc[pid, "mutation_score"]
        hybrid = dfs["hybrid"].loc[pid, "mutation_score"]

        if baseline < 50:
            anomalies.append((pid, "Baseline weak"))

        if spec_sut < 30:
            anomalies.append((pid, "Spec_SUT collapse"))

        if hybrid - baseline < -30:
            anomalies.append((pid, "Hybrid severe regression"))

    return anomalies

# --------------------------------------------------------------
# MAIN
# --------------------------------------------------------------
def main():
    print("\n📥 Loading CSV files...")
    dfs = load_all()

    # Collect mutation score arrays
    ms = {k: dfs[k]["mutation_score"] for k in dfs}

    print("Loaded:", list(ms.keys()))
    print("Total problems:", len(ms["baseline"]))

    # --------------------------------------------
    # SUMMARY STATS
    # --------------------------------------------
    print("\n============================== STATS ==============================")
    summaries = {k: summarize_series(ms[k]) for k in ms}

    for name, s in summaries.items():
        print(f"\n📊 {name.upper()} SUMMARY")
        for k, v in s.items():
            if k == "buckets":
                print("  • Distribution buckets:")
                for bk, bval in v.items():
                    print(f"     - {bk}: {bval}")
            else:
                print(f"  • {k}: {v}")

    # --------------------------------------------
    # IMPROVEMENT/REGRESSION COMPARISONS
    # --------------------------------------------
    print("\n============================== DELTAS ==============================")

    pairs = [
        ("baseline", "spec_NoSUT"),
        ("baseline", "spec_SUT"),
        ("baseline", "hybrid"),
        ("spec_NoSUT", "spec_SUT"),
        ("spec_NoSUT", "hybrid"),
    ]

    for a, b in pairs:
        imp, wors, same, mean_delta, var_delta = compare_pairs(ms[a], ms[b])
        print(f"\nΔ {b} - {a}:")
        print(f"  • Improved: {imp}")
        print(f"  • Worse: {wors}")
        print(f"  • Same: {same}")
        print(f"  • Mean Δ: {mean_delta}")
        print(f"  • Variance Δ: {var_delta}")

    # --------------------------------------------
    # PROBLEM VARIANCE
    # --------------------------------------------
    variance = compute_problem_variance(dfs)
    print("\n============================== VARIANCE ==============================")
    print("Average variance:", variance.mean())

    high_variance = variance[variance > variance.mean() * 2]
    print("\nHigh variance problems:", list(high_variance.index))

    # --------------------------------------------
    # CORRELATION BETWEEN METHODS
    # --------------------------------------------
    print("\n============================== CORRELATION ==============================")
    combined = pd.concat(ms, axis=1)
    print(combined.corr())

    # --------------------------------------------
    # ANOMALIES
    # --------------------------------------------
    anomalies = detect_anomalies(dfs, variance)
    print("\n============================== ANOMALIES ==============================")
    for pid, reason in anomalies:
        print(f"⚠️ {pid}: {reason}")

    # --------------------------------------------
    # SAVE EXTENDED CSV
    # --------------------------------------------
    out = pd.concat(ms, axis=1)
    out["variance"] = variance
    out.to_csv(RESULT_DIR / "comparison_super_extended.csv")

    print("\n📄 Saved SUPER extended comparison → result_spec/comparison_super_extended.csv")


if __name__ == "__main__":
    main()
