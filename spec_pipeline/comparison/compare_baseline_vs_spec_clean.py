import csv
from pathlib import Path
import statistics

BASELINE_FILE = Path("results/metrics.csv")
SPEC_FILE = Path("results/metrics_spec.csv")
OUT_FILE = Path("results/metrics_comparison.csv")
EXCLUDED_FILE = Path("results/metrics_excluded_rows.csv")

def load_csv(path):
    """Load a CSV into a dict keyed by problem_id."""
    if not path.exists():
        print(f"❌ Missing file: {path}")
        return {}

    with open(path, "r") as f:
        rows = list(csv.DictReader(f))

    d = {r["problem_id"]: r for r in rows}
    return d

def safe_float(v):
    """Convert to float, treating N/A or blank as None."""
    try:
        if v in ["N/A", None, "", "None"]:
            return None
        return float(v)
    except:
        return None

def should_exclude(base_val, spec_val, base_cov, spec_cov, base_mut, spec_mut):
    """
    Apply all exclusion rules:
      1. Missing values (None)
      2. Both validity = 0
      3. Both mutation = 0
      4. Missing coverage
    """
    if (
        base_val is None or spec_val is None or
        base_cov is None or spec_cov is None or
        base_mut is None or spec_mut is None
    ):
        return True

    # Both test suites invalid
    if base_val == 0 and spec_val == 0:
        return True

    # Both mutation tests worthless
    if base_mut == 0 and spec_mut == 0:
        return True

    return False

def main():
    print("\n📊 Comparing baseline vs spec-based tests (with auto-exclusion)...\n")

    baseline = load_csv(BASELINE_FILE)
    spec = load_csv(SPEC_FILE)

    if not baseline or not spec:
        print("❌ Missing required result files.")
        return

    comparison_rows = []
    excluded_rows = []

    summary_validity = []
    summary_coverage = []
    summary_mutation = []

    improved_validity = regressed_validity = 0
    improved_coverage = regressed_coverage = 0
    improved_mutation = regressed_mutation = 0

    for pid, base_row in baseline.items():
        if pid not in spec:
            print(f"⚠ Missing spec entry for {pid}")
            continue

        spec_row = spec[pid]

        # Parse values
        base_val = safe_float(base_row["validity_rate"])
        spec_val = safe_float(spec_row["validity_rate"])

        base_cov = safe_float(base_row["coverage"])
        spec_cov = safe_float(spec_row["coverage"])

        base_mut = safe_float(base_row["mutation_score"])
        spec_mut = safe_float(spec_row["mutation_score"])

        # ❌ Apply exclusion logic
        if should_exclude(base_val, spec_val, base_cov, spec_cov, base_mut, spec_mut):
            excluded_rows.append({
                "problem_id": pid,
                "baseline_validity": base_val,
                "spec_validity": spec_val,
                "baseline_coverage": base_cov,
                "spec_coverage": spec_cov,
                "baseline_mutation": base_mut,
                "spec_mutation": spec_mut,
                "reason": "Excluded due to missing/invalid metrics"
            })
            continue

        # Compute diffs
        val_diff = spec_val - base_val
        cov_diff = spec_cov - base_cov
        mut_diff = spec_mut - base_mut

        summary_validity.append(val_diff)
        summary_coverage.append(cov_diff)
        summary_mutation.append(mut_diff)

        if val_diff > 0: improved_validity += 1
        elif val_diff < 0: regressed_validity += 1

        if cov_diff > 0: improved_coverage += 1
        elif cov_diff < 0: regressed_coverage += 1

        if mut_diff > 0: improved_mutation += 1
        elif mut_diff < 0: regressed_mutation += 1

        comparison_rows.append({
            "problem_id": pid,
            "baseline_validity": base_val,
            "spec_validity": spec_val,
            "validity_diff": val_diff,
            "baseline_coverage": base_cov,
            "spec_coverage": spec_cov,
            "coverage_diff": cov_diff,
            "baseline_mutation": base_mut,
            "spec_mutation": spec_mut,
            "mutation_diff": mut_diff
        })

    # Save cleaned comparison
    OUT_FILE.parent.mkdir(exist_ok=True, parents=True)
    with open(OUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "problem_id",
                "baseline_validity", "spec_validity", "validity_diff",
                "baseline_coverage", "spec_coverage", "coverage_diff",
                "baseline_mutation", "spec_mutation", "mutation_diff",
            ]
        )
        writer.writeheader()
        writer.writerows(comparison_rows)

    # Save excluded rows
    with open(EXCLUDED_FILE, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=list(excluded_rows[0].keys()) if excluded_rows else ["problem_id", "reason"]
        )
        writer.writeheader()
        writer.writerows(excluded_rows)

    print(f"📄 Clean comparison saved to: {OUT_FILE}")
    print(f"🗑️ Excluded rows saved to:   {EXCLUDED_FILE}\n")

    # Summary stats
    print("============== SUMMARY ==============\n")
    if summary_validity:
        print(f"Average validity improvement:   {statistics.mean(summary_validity):.2f}%")
        print(f"Improved: {improved_validity}  |  Regressed: {regressed_validity}")
    else:
        print("Validity: No comparable values")

    if summary_coverage:
        print(f"Average coverage improvement:   {statistics.mean(summary_coverage):.2f}%")
        print(f"Improved: {improved_coverage}  |  Regressed: {regressed_coverage}")
    else:
        print("Coverage: No comparable values")

    if summary_mutation:
        print(f"Average mutation improvement:   {statistics.mean(summary_mutation):.2f}%")
        print(f"Improved: {improved_mutation}  |  Regressed: {regressed_mutation}")
    else:
        print("Mutation: No comparable values")

    print("\n======================================")
    print("Comparison complete! Clean dataset ready.\n")


if __name__ == "__main__":
    main()
