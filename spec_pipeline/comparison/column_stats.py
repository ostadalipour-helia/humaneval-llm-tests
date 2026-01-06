#!/usr/bin/env python3
"""
Column-level metrics analyzer for all four suites:
- baseline
- spec_NoSUT
- spec_SUT
- hybrid

Computes aggregated statistics PER COLUMN (not per problem):
- mean
- variance
- median
- std
- min/max
- zeros
- missing values
- histogram buckets
- correlation matrix
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV_DIR = ROOT / "result_spec"

FILES = {
    "baseline": CSV_DIR / "metrics_baseline.csv",
    "spec_NoSUT": CSV_DIR / "metrics_spec_NoSUT.csv",
    "spec_SUT": CSV_DIR / "metrics_spec_SUT.csv",
    "hybrid": CSV_DIR / "metrics_hybrid.csv",
}

METRIC_COLS = ["validity_rate", "coverage", "mutation_score"]


def describe_column(series: pd.Series):
    """Return a dictionary of column-level statistics."""
    clean = series.dropna()

    hist = {
        "0–20": ((clean >= 0) & (clean < 20)).sum(),
        "20–40": ((clean >= 20) & (clean < 40)).sum(),
        "40–60": ((clean >= 40) & (clean < 60)).sum(),
        "60–80": ((clean >= 60) & (clean < 80)).sum(),
        "80–100": ((clean >= 80) & (clean <= 100)).sum(),
    }

    return {
        "count": len(series),
        "missing": series.isna().sum(),
        "zeros": (series == 0).sum(),
        "mean": clean.mean(),
        "median": clean.median(),
        "variance": clean.var(),
        "std": clean.std(),
        "min": clean.min(),
        "max": clean.max(),
        "p25": clean.quantile(0.25),
        "p75": clean.quantile(0.75),
        "hist_buckets": hist,
    }


def main():
    print("\n=========== Column-Level Analysis ===========\n")

    # Load all CSVs
    dfs = {name: pd.read_csv(path) for name, path in FILES.items()}

    # Combine into one wide table
    wide = pd.DataFrame({"problem_id": dfs["baseline"]["problem_id"]})

    for name, df in dfs.items():
        for col in METRIC_COLS:
            wide[f"{name}_{col}"] = df[col]

    print(f"Loaded CSV columns: {list(wide.columns)}\n")

    # Compute stats per column
    results = {}
    for col in wide.columns:
        if col == "problem_id":
            continue
        results[col] = describe_column(wide[col])

    # Print summary
    for col, stats in results.items():
        print(f"\n📊 COLUMN: {col}")
        for k, v in stats.items():
            if k == "hist_buckets":
                print("  • Distribution buckets:")
                for bucket, count in v.items():
                    print(f"     - {bucket}: {count}")
            else:
                print(f"  • {k}: {v}")

    # Correlation matrix
    metric_cols = [c for c in wide.columns if c != "problem_id"]
    corr = wide[metric_cols].corr()

    print("\n=========== CORRELATION MATRIX ===========\n")
    print(corr)

    # Save output files
    out_stats = CSV_DIR / "column_stats.csv"
    pd.DataFrame(results).T.to_csv(out_stats)
    print(f"\n📄 Saved column-level stats → {out_stats}")

    out_corr = CSV_DIR / "column_correlation.csv"
    corr.to_csv(out_corr)
    print(f"📄 Saved correlation matrix → {out_corr}\n")

    print("\n🎉 DONE — Column-level summary generated!\n")



if __name__ == "__main__":
    main()
