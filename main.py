from prompt_sets import get_baseline_prompts
from clip_classifier import average_group_similarity
from evaluate import evaluate_dataset, classify_image
import json
from sklearn.metrics import classification_report

def main():
    # 1. Load prompt groups
    prompts = get_baseline_prompts()

    # 2. Define which prompt groups map to real vs fake
    real_groups = ["generic", "technical"]
    fake_groups = ["forensic", "layman"]

    # 3. Set dataset directory
    dataset_dir = "./Dataset"

    # 4. Run evaluation
    results = evaluate_dataset(dataset_dir, prompts, real_groups, fake_groups)

    # 5. Save results
    with open("results/results.json", "w") as f:
        json.dump(results, f, indent=2)

    # 6. Compute and print evaluation metrics
    y_true = [r["true"] for r in results]
    y_pred = [r["pred"] for r in results]
    print("\nEvaluation Metrics:")
    print(classification_report(y_true, y_pred, target_names=["Real", "Fake"]))

if __name__ == "__main__":
    main()