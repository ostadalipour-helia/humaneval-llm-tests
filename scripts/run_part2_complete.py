import subprocess
import sys
import json
from pathlib import Path

# Checkpoint file to track completed steps
CHECKPOINT_FILE = Path("results/pipeline_checkpoint.json")

def load_checkpoint():
    """Load checkpoint of completed steps."""
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, 'r') as f:
            return json.load(f)
    return {"completed_steps": []}

def save_checkpoint(step_name):
    """Save checkpoint after completing a step."""
    checkpoint = load_checkpoint()
    if step_name not in checkpoint["completed_steps"]:
        checkpoint["completed_steps"].append(step_name)
    
    CHECKPOINT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CHECKPOINT_FILE, 'w') as f:
        json.dump(checkpoint, f, indent=2)

def is_step_completed(step_name):
    """Check if a step was already completed."""
    checkpoint = load_checkpoint()
    return step_name in checkpoint["completed_steps"]

def run_script(script_name, step_name, description):
    """Run a Python script and handle errors."""
    
    # Check if already completed
    if is_step_completed(step_name):
        print(f"\n{'='*60}")
        print(f"✓ SKIPPING: {description}")
        print(f"  (Already completed - found in checkpoint)")
        print(f"{'='*60}\n")
        return True
    
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"{'='*60}\n")
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            check=True
        )
        print(f"✅ {description} completed successfully!")
        
        # Save checkpoint
        save_checkpoint(step_name)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with error code {e.returncode}")
        return False
    except Exception as e:
        print(f"❌ Error running {description}: {e}")
        return False

def reset_checkpoint():
    """Reset checkpoint to start fresh."""
    if CHECKPOINT_FILE.exists():
        CHECKPOINT_FILE.unlink()
        print("✓ Checkpoint reset - will run all steps")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Run Part 2 Complete Pipeline')
    parser.add_argument('--reset', action='store_true', 
                       help='Reset checkpoint and run all steps from beginning')
    parser.add_argument('--skip-to', type=str, 
                       help='Skip to specific step: generate|fix|coverage|enhance|evaluate')
    args = parser.parse_args()
    
    if args.reset:
        reset_checkpoint()
    
    print("\n" + "="*60)
    print(" "*15 + "PART 2 COMPLETE PIPELINE")
    print("="*60)
    
    # Show checkpoint status
    checkpoint = load_checkpoint()
    if checkpoint["completed_steps"]:
        print("\n📋 Previously completed steps:")
        for step in checkpoint["completed_steps"]:
            print(f"   ✓ {step}")
        print()
    
    scripts = [
        ("scripts/generate_llm_solutions.py", "step1_generate", "Step 1: Generate LLM Solutions"),
        ("scripts/iterative_fix.py", "step2_fix", "Step 2-3: Iterative Test Fixing"),
        ("scripts/calculate_coverage_part2.py", "step3_coverage", "Step 4: Calculate Coverage After Fixing"),
        ("scripts/coverage_enhance.py", "step4_enhance", "Step 5: Coverage Enhancement"),
        ("scripts/evaluate_part2.py", "step5_evaluate", "Step 6: Generate Final Report"),
    ]
    
    # Handle skip-to option
    start_index = 0
    if args.skip_to:
        skip_map = {
            'generate': 0,
            'fix': 1,
            'coverage': 2,
            'enhance': 3,
            'evaluate': 4
        }
        if args.skip_to in skip_map:
            start_index = skip_map[args.skip_to]
            print(f"\n⏩ Skipping to: {scripts[start_index][2]}\n")
        else:
            print(f"\n⚠️  Unknown step: {args.skip_to}")
            print(f"   Valid options: generate, fix, coverage, enhance, evaluate\n")
            return
    
    results = []
    
    for i, (script, step_name, description) in enumerate(scripts):
        if i < start_index:
            continue
            
        success = run_script(script, step_name, description)
        results.append((description, success))
        
        if not success:
            print(f"\n⚠️  Pipeline stopped due to failure in: {description}")
            print(f"\nTo resume from this step, run:")
            print(f"   python scripts/run_part2_complete.py")
            print(f"\nTo reset and start over, run:")
            print(f"   python scripts/run_part2_complete.py --reset")
            break
    
    # Print final summary
    print("\n" + "="*60)
    print(" "*15 + "PIPELINE SUMMARY")
    print("="*60)
    
    for description, success in results:
        status = "✅ SUCCESS" if success else "❌ FAILED"
        print(f"{status}: {description}")
    
    all_success = all(success for _, success in results)
    
    if all_success:
        print("\n🎉 All steps completed successfully!")
        print("\n📊 Check the following files for results:")
        print("   - results/fixing_log.json")
        print("   - results/coverage_before_enhancement.csv")
        print("   - results/coverage_improvement.csv")
        print("   - results/part2_summary.json")
        
        # Clear checkpoint after full success
        print("\n✓ Pipeline complete - checkpoint cleared")
        reset_checkpoint()
    else:
        print("\n⚠️  Some steps failed. The checkpoint has been saved.")
        print("   Run the script again to resume from where it stopped.")
    
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()