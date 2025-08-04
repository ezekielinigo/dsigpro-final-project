import os
import json
from tqdm import tqdm
from clip_classifier import compute_similarity, encode_prompts
import matplotlib.pyplot as plt

def evaluate_prompt_type(dataset_dir, prompt_type_dict, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    real_prompts = prompt_type_dict["real"]
    fake_prompts = prompt_type_dict["fake"]
    encoded_real = encode_prompts(real_prompts)
    encoded_fake = encode_prompts(fake_prompts)

    results = []
    score_diffs = []

    for label_str in ["real", "fake"]:
        label = 0 if label_str == "real" else 1
        folder = os.path.join(dataset_dir, label_str)
        image_list = os.listdir(folder)

        for img in tqdm(image_list, desc=f"{label_str.upper()} images"):
            path = os.path.join(folder, img)

            real_scores = compute_similarity(path, encoded_real)
            fake_scores = compute_similarity(path, encoded_fake)

            real_score = real_scores.mean()
            fake_score = fake_scores.mean()
            margin = fake_score - real_score
            pred = 1 if margin > 0 else 0

            top_real_idx = real_scores.argmax()
            top_fake_idx = fake_scores.argmax()

            top_real_prompt = real_prompts[top_real_idx]
            top_fake_prompt = fake_prompts[top_fake_idx]

            results.append({
                "filename": img,
                "true": label,
                "pred": pred,
                "real_score": float(real_score),
                "fake_score": float(fake_score),
                "score_margin": float(margin),
                "top_real_prompt": top_real_prompt,
                "top_fake_prompt": top_fake_prompt,
                "top_real_score": float(real_scores[top_real_idx]),
                "top_fake_score": float(fake_scores[top_fake_idx])
            })

            # Save intermediate results
            with open(save_path, "w") as f:
                json.dump(results, f, indent=2)

            score_diffs.append(margin)

    # Plot histogram of score margins
    plt.hist(score_diffs, bins=40, color='skyblue', edgecolor='black')
    plt.axvline(0, color='red', linestyle='--', label='Decision Boundary')
    plt.title("Fake - Real Similarity Score Differences")
    plt.xlabel("Score Difference")
    plt.ylabel("Number of Images")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path.replace(".json", "_margin_hist.png"))
    plt.close()

    return results
