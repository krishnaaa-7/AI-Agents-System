from validation.agreement import agreement_score

class ValidationAgent:
    def validate(self, fusion_output):
        text_ans = fusion_output["text_summary"]
        vision_ans = fusion_output["visual_summary"]

        agreement = agreement_score(text_ans, vision_ans)

        return {
            "agreement_score": agreement,
            "status": "ok" if agreement >= 0.75 else "review"
        }

