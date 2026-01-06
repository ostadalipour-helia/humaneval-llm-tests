import csv
from pathlib import Path
import statistics

BASELINE_FILE = Path("results/metrics.csv")
SPEC_FILE = Path("results/metrics_spec.csv")
OUT_FILE = Path("results/metrics_comparison.csv")

def load_csv(path):
    """Load a CSV into a dict keyed by problem_id."""
    if not path.exists():
        print(f"❌ Missing file: {path}")
        return {}

    with open(path, "r") as f:
        rows = list(csv.DictReader(f))

    d = {}
    for r in rows:
        pid = r["problem_id"]
        d[pid] = r
    return d


def safe_float(v):
    """Convert value to float, return None if N/A."""
    try:
        if v in ["N/A", None, ""]:
            return None
        return float(v)
    except:
        return None


def main():
    print("\n📊 Comparing baseline vs spec-based tests...\n")

    baseline = load_csv(BASELINE_FILE)
    spec = load_csv(SPEC_FILE)

    if not baseline or not spec:
        print("❌ Missing required result files.")
        return

    comparison_rows = []
    summary_validity = []
    summary_coverage = []
    summary_mutation = []

    improved_validity = 0
    improved_coverage = 0
    improved_mutation = 0

    regressed_validity = 0
    regressed_coverage = 0
    regressed_mutation = 0

    for pid in baseline:
        if pid not in spec:
            print(f"⚠ Warning: Missing spec result for {pid}")
            continue

        base_row = baseline[pid]
        spec_row = spec[pid]

        # Parse values safely
        base_val = safe_float(base_row["validity_rate"])
        spec_val = safe_float(spec_row["validity_rate"])

        base_cov = safe_float(base_row["coverage"])
        spec_cov = safe_float(spec_row["coverage"])

        base_mut = safe_float(base_row["mutation_score"])
        spec_mut = safe_float(spec_row["mutation_score"])

        # Compute diffs
        val_diff = None
        cov_diff = None
        mut_diff = None

        if base_val is not None and spec_val is not None:
            val_diff = spec_val - base_val
            summary_validity.append(val_diff)
            if val_diff > 0: improved_validity += 1
            elif val_diff < 0: regressed_validity += 1

        if base_cov is not None and spec_cov is not None:
            cov_diff = spec_cov - base_cov
            summary_coverage.append(cov_diff)
            if cov_diff > 0: improved_coverage += 1
            elif cov_diff < 0: regressed_coverage += 1

        if base_mut is not None and spec_mut is not None:
            mut_diff = spec_mut - base_mut
            summary_mutation.append(mut_diff)
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

    # Save CSV
    with open(OUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "problem_id",
                "baseline_validity", "spec_validity", "validity_diff",
                "baseline_coverage", "spec_coverage", "coverage_diff",
                "baseline_mutation", "spec_mutation", "mutation_diff",
            ],
        )
        writer.writeheader()
        writer.writerows(comparison_rows)

    print(f"📄 CSV saved to {OUT_FILE}\n")

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

    print("\n======================================\n")
    print("Comparison complete!")
    print("You can now use metrics_comparison.csv for your paper/report.\n")


if __name__ == "__main__":
    main()
