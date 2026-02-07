from vlm.llava_agent import LLaVAAgent

class VisionAgent:
    def __init__(self):
        self.llava = LLaVAAgent()

    def run(self, image):
        # image = PIL Image or image path
        explanation = self.llava.analyze(
            image,
            "Explain this diagram or visual element"
        )

        return {
            "visual_explanation": explanation,
            "cv_confidence": 0.85  # placeholder (can improve later)
        }
