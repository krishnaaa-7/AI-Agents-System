from transformers import LlavaProcessor, LlavaForConditionalGeneration
import torch
from PIL import Image


class LLaVAAgent:
    def __init__(self):
        self.processor = LlavaProcessor.from_pretrained(
            "llava-hf/llava-1.5-7b-hf"
        )
        self.model = LlavaForConditionalGeneration.from_pretrained(
            "llava-hf/llava-1.5-7b-hf",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto"
        )

    def analyze(self, image, question: str):
        """
        image: PIL.Image.Image OR image path (str)
        question: prompt string
        """
        if isinstance(image, str):
            image = Image.open(image)

        inputs = self.processor(
            images=image,
            text=question,
            return_tensors="pt"
        ).to(self.model.device)

        output = self.model.generate(
            **inputs,
            max_new_tokens=200
        )

        return self.processor.decode(
            output[0],
            skip_special_tokens=True
        )
