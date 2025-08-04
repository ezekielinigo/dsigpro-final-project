# 

import os
import json
from sklearn.metrics import classification_report
from clip_classifier import average_group_similarity
from prompt_sets import get_baseline_prompts

def classify_image(similarity_dict, real_groups, fake_groups):
    real_score = sum(similarity_dict[g]["mean"] for g in real_groups) / len(real_groups)
    fake_score = sum(similarity_dict[g]["mean"] for g in fake_groups) / len(fake_groups)
    return 0 if real_score > fake_score else 1

def evaluate_dataset(dataset_dir, prompt_groups, real_groups, fake_groups):
    results = []
    for label_str in ["real", "fake"]:
        label = 0 if label_str == "real" else 1
        folder = os.path.join(dataset_dir, label_str)
        for img in os.listdir(folder):
            path = os.path.join(folder, img)
            sims = average_group_similarity(path, prompt_groups)
            pred = classify_image(sims, real_groups, fake_groups)
            results.append({"filename": img, "true": label, "pred": pred, "scores": sims})
    return results

def main():
    prompts = get_baseline_prompts()
    dataset_dir = "./Dataset"
    real_groups = ["generic", "technical"]  # example
    fake_groups = ["forensic", "layman"]

    results = evaluate_dataset(dataset_dir, prompts, real_groups, fake_groups)

    # Save results
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    # Compute metrics
    y_true = [r["true"] for r in results]
    y_pred = [r["pred"] for r in results]
    print(classification_report(y_true, y_pred, target_names=["Real", "Fake"]))

if __name__ == "__main__":
    main()
