import os
import json
from prompt_sets import *
from evaluate import evaluate_prompt_type
from sklearn.metrics import classification_report

LLM_SOURCES = {
    "chatgpt4o": get_chatgpt4o_prompts,
    "chatgpt4pt5": get_chatgpt4pt5_prompts,
    "deepseekr1": get_deepseekr1_prompts,
    "gemini2pt5pro": get_gemini2pt5pro_prompts,
    "claudesonnet4": get_claudesonnet4_prompts
}

def main():
    dataset_dir = "./Dataset"
    results_dir = "./results"
    os.makedirs(results_dir, exist_ok=True)

    for llm_name, prompt_loader in LLM_SOURCES.items():
        prompt_set = prompt_loader()

        for prompt_type, type_prompts in prompt_set.items():
            print(f"\n>>> Evaluating: {llm_name} – {prompt_type}")
            save_path = os.path.join(results_dir, f"{llm_name}_{prompt_type}.json")

            if os.path.exists(save_path):
                print("  ↪ Skipping (already computed)")
                continue

            results = evaluate_prompt_type(dataset_dir, type_prompts, save_path)

            y_true = [r["true"] for r in results]
            y_pred = [r["pred"] for r in results]

            print(classification_report(y_true, y_pred, target_names=["Real", "Fake"]))

if __name__ == "__main__":
    main()
