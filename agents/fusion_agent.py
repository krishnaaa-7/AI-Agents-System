class FusionAgent:
    def fuse(self, vision_output, text_output):
        return {
            "text_summary": text_output,
            "visual_summary": vision_output["visual_explanation"]
        }
