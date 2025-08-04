# used for the actual CLIP

import open_clip
import torch
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

model, _, preprocess = open_clip.create_model_and_transforms("ViT-B-32", pretrained="laion2b_s34b_b79k")
tokenizer = open_clip.get_tokenizer("ViT-B-32")
model = model.to(device).eval()

def compute_similarity(image_path, prompts):
    image = preprocess(Image.open(image_path).convert("RGB")).unsqueeze(0).to(device)
    text_inputs = tokenizer(prompts).to(device)
    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text_inputs)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        similarity = image_features @ text_features.T
    return similarity.squeeze(0).cpu().numpy()

def average_group_similarity(image_path, prompt_groups):
    result = {}
    for group, prompts in prompt_groups.items():
        sims = compute_similarity(image_path, prompts)
        result[group] = {
            "mean": float(sims.mean()),
            "std": float(sims.std())
        }
    return result
