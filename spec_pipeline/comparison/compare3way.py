import csv
from pathlib import Path
import statistics

###############################################
# CONFIG —–––> CHANGE THESE THREE PATHS ONLY
###############################################

BASELINE_FILE = Path("results/metrics.csv")
SPEC_FILE = Path("results/metrics_spec.csv")
HYBRID_FILE = Path("results/metrics_spec_hybrid.csv")

OUTPUT_FILE = Path("results/metrics_three_way_comparison.csv")

###############################################


def load_csv(path):
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
    try:
        if v in ["", "None", "N/A", None]:
            return None
        return float(v)
    except:
        return None


def diff(a, b):
    if a is None or b is None:
        return None
    return b - a


def main():
    print("\n📊 3-WAY COMPARISON: baseline vs spec vs hybrid-clean\n")

    baseline = load_csv(BASELINE_FILE)
    spec = load_csv(SPEC_FILE)
    hybrid = load_csv(HYBRID_FILE)

    if not baseline or not spec or not hybrid:
        print("❌ Missing required CSVs. Fix paths and try again.")
        return

    rows = []
    summary = {
        "val_spec_better": 0,
        "val_hybrid_better": 0,
        "cov_spec_better": 0,
        "cov_hybrid_better": 0,
        "mut_spec_better": 0,
        "mut_hybrid_better": 0,
    }

    val_diffs_spec = []
    val_diffs_hybrid = []
    cov_diffs_spec = []
    cov_diffs_hybrid = []
    mut_diffs_spec = []
    mut_diffs_hybrid = []

    all_pids = sorted(set(baseline.keys()) & set(spec.keys()) & set(hybrid.keys()))

    for pid in all_pids:
        b = baseline[pid]
        s = spec[pid]
        h = hybrid[pid]

        # Parse numbers
        b_val = safe_float(b["validity_rate"])
        s_val = safe_float(s["validity_rate"])
        h_val = safe_float(h["validity_rate"])

        b_cov = safe_float(b["coverage"])
        s_cov = safe_float(s["coverage"])
        h_cov = safe_float(h["coverage"])

        b_mut = safe_float(b["mutation_score"])
        s_mut = safe_float(s["mutation_score"])
        h_mut = safe_float(h["mutation_score"])

        # Compute diffs
        ds_val = diff(b_val, s_val)
        dh_val = diff(b_val, h_val)

        ds_cov = diff(b_cov, s_cov)
        dh_cov = diff(b_cov, h_cov)

        ds_mut = diff(b_mut, s_mut)
        dh_mut = diff(b_mut, h_mut)

        # track summary
        if ds_val is not None:
            val_diffs_spec.append(ds_val)
            if ds_val > 0: summary["val_spec_better"] += 1

        if dh_val is not None:
            val_diffs_hybrid.append(dh_val)
            if dh_val > 0: summary["val_hybrid_better"] += 1

        if ds_cov is not None:
            cov_diffs_spec.append(ds_cov)
            if ds_cov > 0: summary["cov_spec_better"] += 1

        if dh_cov is not None:
            cov_diffs_hybrid.append(dh_cov)
            if dh_cov > 0: summary["cov_hybrid_better"] += 1

        if ds_mut is not None:
            mut_diffs_spec.append(ds_mut)
            if ds_mut > 0: summary["mut_spec_better"] += 1

        if dh_mut is not None:
            mut_diffs_hybrid.append(dh_mut)
            if dh_mut > 0: summary["mut_hybrid_better"] += 1

        rows.append({
            "problem_id": pid,

            "baseline_validity": b_val, "spec_validity": s_val, "hybrid_validity": h_val,
            "spec_vs_baseline_validity_diff": ds_val,
            "hybrid_vs_baseline_validity_diff": dh_val,

            "baseline_coverage": b_cov, "spec_coverage": s_cov, "hybrid_coverage": h_cov,
            "spec_vs_baseline_coverage_diff": ds_cov,
            "hybrid_vs_baseline_coverage_diff": dh_cov,

            "baseline_mutation": b_mut, "spec_mutation": s_mut, "hybrid_mutation": h_mut,
            "spec_vs_baseline_mutation_diff": ds_mut,
            "hybrid_vs_baseline_mutation_diff": dh_mut,
        })

    # Save CSV
    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"📄 Saved combined comparison to: {OUTPUT_FILE}")

    print("\n===================================")
    print("RESULT SUMMARY")
    print("===================================\n")

    # Validity improvement summary
    if val_diffs_spec:
        print(f"Spec vs Baseline validity (mean):  {statistics.mean(val_diffs_spec):.2f}")
        print(f"Spec better in {summary['val_spec_better']} cases")
    if val_diffs_hybrid:
        print(f"Hybrid vs Baseline validity (mean): {statistics.mean(val_diffs_hybrid):.2f}")
        print(f"Hybrid better in {summary['val_hybrid_better']} cases\n")

    # Coverage summary
    if cov_diffs_spec:
        print(f"Spec vs Baseline coverage (mean):  {statistics.mean(cov_diffs_spec):.2f}")
        print(f"Spec better in {summary['cov_spec_better']} cases")
    if cov_diffs_hybrid:
        print(f"Hybrid vs Baseline coverage (mean): {statistics.mean(cov_diffs_hybrid):.2f}")
        print(f"Hybrid better in {summary['cov_hybrid_better']} cases\n")

    # Mutation summary
    if mut_diffs_spec:
        print(f"Spec vs Baseline mutation (mean):  {statistics.mean(mut_diffs_spec):.2f}")
        print(f"Spec better in {summary['mut_spec_better']} cases")
    if mut_diffs_hybrid:
        print(f"Hybrid vs Baseline mutation (mean): {statistics.mean(mut_diffs_hybrid):.2f}")
        print(f"Hybrid better in {summary['mut_hybrid_better']} cases")

    print("\n===================================")
    print("3-WAY COMPARISON COMPLETE")
    print("===================================\n")


if __name__ == "__main__":
    main()
