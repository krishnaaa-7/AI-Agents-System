from fastapi import FastAPI, UploadFile, File, HTTPException
import tempfile
import os

from document.loader import load_pdf
from agents.vision_agent import VisionAgent
from agents.text_agent import TextAgent
from agents.fusion_agent import FusionAgent
from agents.validation_agent import ValidationAgent
from validation.confidence import calculate_confidence

app = FastAPI(
    title="Multi-Modal Document Intelligence API",
    description="Processes PDF documents using Vision + Text + Fusion agents",
    version="1.0.0"
)

# Initialize agents once (good practice)
vision_agent = VisionAgent()
text_agent = TextAgent()
fusion_agent = FusionAgent()
validation_agent = ValidationAgent()


# ---------------------------
# Health / Home Endpoint
# ---------------------------
@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Multi-Modal Document Intelligence API is live",
        "docs": "/docs"
    }


# ---------------------------
# Document Processing Endpoint
# ---------------------------
@app.post("/process")
async def process_document(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    tmp_path = None

    try:
        # 1️⃣ Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        # 2️⃣ Load PDF (images + text)
        images, texts = load_pdf(tmp_path)

        if not images and not texts:
            raise HTTPException(status_code=400, detail="Failed to extract content from PDF")

        # 3️⃣ Run agents (first page for demo simplicity)
        vision_output = vision_agent.run(images[0]) if images else {
            "visual_explanation": "",
            "cv_confidence": 0.0
        }

        text_output = text_agent.analyze(texts[0] or "") if texts else ""
        ocr_confidence = 0.9  # placeholder (can be returned from TextAgent later)

        fusion_output = fusion_agent.fuse(
            vision_output=vision_output,
            text_output=text_output
        )

        validation_output = validation_agent.validate(fusion_output)

        # 4️⃣ Calculate final confidence
        confidence = calculate_confidence(
            ocr_conf=ocr_confidence,
            cv_conf=vision_output["cv_confidence"],
            agreement=validation_output["agreement_score"]
        )

        # 5️⃣ Return full pipeline output
        return {
            "file_name": file.filename,
            "status": validation_output["status"],
            "confidence": confidence,
            "vision_output": vision_output,
            "text_output": text_output,
            "fusion_output": fusion_output,
            "validation": validation_output
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # 6️⃣ Cleanup temp file
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)

