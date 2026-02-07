import clip
import torch
from PIL import Image

class ImageEmbedder:
    def __init__(self, device="cpu"):
        self.device = device
        self.model, self.preprocess = clip.load(
            "ViT-B/32", device=device
        )

    def embed(self, image_path: str):
        image = self.preprocess(Image.open(image_path)).unsqueeze(0).to(self.device)
        with torch.no_grad():
            embedding = self.model.encode_image(image)
        return embedding.cpu().numpy()[0]
