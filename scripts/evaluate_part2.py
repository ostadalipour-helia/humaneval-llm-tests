import json
import csv
from pathlib import Path

RESULTS_DIR = Path("results")


def load_json(filename):
    """Load JSON file."""
    filepath = RESULTS_DIR / filename
    if filepath.exists():
        with open(filepath, 'r') as f:
            return json.load(f)
    return None


def load_csv(filename):
    """Load CSV file."""
    filepath = RESULTS_DIR / filename
    if filepath.exists():
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)
    return None


def analyze_fixing_results():
    """Analyze test fixing results."""
    fixing_log = load_json("fixing_log.json")
    
    if not fixing_log:
        print("❌ fixing_log.json not found")
        return None
    
    total_tests = sum(s['total_tests'] for s in fixing_log)
    total_passed = sum(s['passed_initially'] for s in fixing_log)
    total_fixed = sum(s['fixed'] for s in fixing_log)
    total_discarded = sum(s['discarded'] for s in fixing_log)
    
    return {
        "total_tests": total_tests,
        "passed_initially": total_passed,
        "fixed": total_fixed,
        "discarded": total_discarded,
        "final_passing": total_passed + total_fixed,
        "pass_rate_initial": (total_passed / total_tests * 100) if total_tests > 0 else 0,
        "pass_rate_final": ((total_passed + total_fixed) / total_tests * 100) if total_tests > 0 else 0
    }


def analyze_coverage_improvement():
    """Analyze coverage improvement results."""
    improvement_data = load_csv("coverage_improvement.csv")
    
    if not improvement_data:
        print("❌ coverage_improvement.csv not found")
        return None
    
    valid_data = []
    for row in improvement_data:
        try:
            if row['coverage_before'] != 'N/A' and row['coverage_after'] != 'N/A':
                before = float(row['coverage_before'])
                after = float(row['coverage_after'])
                valid_data.append({
                    'problem_id': row['problem_id'],
                    'before': before,
                    'after': after,
                    'improvement': after - before
                })
        except (ValueError, KeyError):
            continue
    
    if not valid_data:
        return None
    
    avg_before = sum(d['before'] for d in valid_data) / len(valid_data)
    avg_after = sum(d['after'] for d in valid_data) / len(valid_data)
    avg_improvement = avg_after - avg_before
    
    # Count improvements
    improved = sum(1 for d in valid_data if d['improvement'] > 0)
    no_change = sum(1 for d in valid_data if d['improvement'] == 0)
    decreased = sum(1 for d in valid_data if d['improvement'] < 0)
    
    return {
        "total_problems": len(valid_data),
        "avg_coverage_before": avg_before,
        "avg_coverage_after": avg_after,
        "avg_improvement": avg_improvement,
        "improved_count": improved,
        "no_change_count": no_change,
        "decreased_count": decreased,
        "max_improvement": max(d['improvement'] for d in valid_data),
        "min_improvement": min(d['improvement'] for d in valid_data)
    }


def generate_report():
    """Generate comprehensive Part 2 report."""
    print("\n" + "="*60)
    print(" "*15 + "PART 2 EVALUATION REPORT")
    print("="*60)
    
    # Section 1: Test Fixing Results
    print("\n📋 SECTION 1: ITERATIVE TEST FIXING")
    print("-" * 60)
    
    fixing_results = analyze_fixing_results()
    if fixing_results:
        print(f"Total tests generated:        {fixing_results['total_tests']}")
        print(f"Passed initially:             {fixing_results['passed_initially']} "
              f"({fixing_results['pass_rate_initial']:.2f}%)")
        print(f"Fixed successfully:           {fixing_results['fixed']}")
        print(f"Discarded (unfixable):        {fixing_results['discarded']}")
        print(f"Final passing tests:          {fixing_results['final_passing']} "
              f"({fixing_results['pass_rate_final']:.2f}%)")
        print(f"\nImprovement: {fixing_results['pass_rate_final'] - fixing_results['pass_rate_initial']:.2f}% "
              f"({fixing_results['fixed']} tests fixed)")
    else:
        print("❌ No fixing results available")
    
    # Section 2: Coverage Enhancement
    print("\n\n📊 SECTION 2: COVERAGE ENHANCEMENT")
    print("-" * 60)
    
    coverage_results = analyze_coverage_improvement()
    if coverage_results:
        print(f"Problems analyzed:            {coverage_results['total_problems']}")
        print(f"\nCoverage before enhancement:  {coverage_results['avg_coverage_before']:.2f}%")
        print(f"Coverage after enhancement:   {coverage_results['avg_coverage_after']:.2f}%")
        print(f"Average improvement:          {coverage_results['avg_improvement']:.2f}%")
        print(f"\nProblems improved:            {coverage_results['improved_count']}")
        print(f"Problems unchanged:           {coverage_results['no_change_count']}")
        print(f"Problems decreased:           {coverage_results['decreased_count']}")
        print(f"\nMax improvement:              {coverage_results['max_improvement']:.2f}%")
        print(f"Min improvement:              {coverage_results['min_improvement']:.2f}%")
    else:
        print("❌ No coverage enhancement results available")
    
    # Section 3: Overall Summary
    print("\n\n✨ OVERALL SUMMARY")
    print("-" * 60)
    
    if fixing_results and coverage_results:
        print(f"Initial test pass rate:       {fixing_results['pass_rate_initial']:.2f}%")
        print(f"Final test pass rate:         {fixing_results['pass_rate_final']:.2f}%")
        print(f"Test fixing improvement:      {fixing_results['pass_rate_final'] - fixing_results['pass_rate_initial']:.2f}%")
        print(f"\nInitial coverage:             {coverage_results['avg_coverage_before']:.2f}%")
        print(f"Final coverage:               {coverage_results['avg_coverage_after']:.2f}%")
        print(f"Coverage improvement:         {coverage_results['avg_improvement']:.2f}%")
        
        print(f"\n🎯 Total Quality Improvement:")
        total_improvement = (fixing_results['pass_rate_final'] - fixing_results['pass_rate_initial']) + \
                           coverage_results['avg_improvement']
        print(f"   Combined metric improvement: {total_improvement:.2f}%")
    
    print("\n" + "="*60)
    print("Report generation complete!")
    print("="*60 + "\n")
    
    # Save summary to file
    summary = {
        "test_fixing": fixing_results,
        "coverage_enhancement": coverage_results
    }
    
    with open(RESULTS_DIR / "part2_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    
    print(f"📄 Summary saved to: {RESULTS_DIR / 'part2_summary.json'}")


def main():
    generate_report()


if __name__ == "__main__":
    main()
