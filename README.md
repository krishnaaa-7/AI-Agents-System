## 🧠 Multi-Modal Document Intelligence System

Vision + Language + Agents for Document Understanding

This project implements a production-style multi-modal document intelligence system that combines computer vision, OCR, and LLMs using a multi-agent architecture. The system processes real-world PDF documents containing text, images, tables, and diagrams, and produces validated, confidence-scored outputs.

Built as part of the QuickPlans AI Multi-Modal Challenge.

## 🚀 Features

## 📄 PDF document ingestion (scanned & digital)

## 👁️ Vision understanding using a Vision-Language Model (LLaVA)

## 📝 Text understanding via OCR + LLM reasoning

## 🤝 Multi-agent architecture:

Vision Agent

Text Agent

Fusion Agent

Validation Agent

🔎 Layout-aware processing (images + text)

📊 Multi-modal confidence scoring

🌐 REST API using FastAPI

📦 Clean, modular, production-ready Python code

## 🏗️ Architecture Overview
PDF Document
     ↓
Document Loader
     ↓
PDF → Images + Text
     ↓
┌───────────────┬───────────────┐
│  Vision Agent │   Text Agent  │
│  (LLaVA + CV) │ (OCR + LLM)   │
└───────────────┴───────────────┘
            ↓
        Fusion Agent
            ↓
      Validation Agent
            ↓
   Confidence Scoring System
            ↓
        JSON API Output

## 📁 Project Structure
multi_modal_doc_ai/
│
├── api/
│   └── main.py                 # FastAPI entrypoint
│
├── agents/
│   ├── vision_agent.py         # Vision + VLM reasoning
│   ├── text_agent.py           # OCR + text reasoning
│   ├── fusion_agent.py         # Multi-modal fusion
│   └── validation_agent.py     # Cross-modal validation
│
├── cv/
│   ├── ocr.py                  # OCR logic
│   ├── layout_detector.py      # Layout analysis
│   └── utils.py
│
├── document/
│   └── loader.py               # PDF → images + text
│
├── validation/
│   └── confidence.py           # Confidence scoring
│
├── vlm/
│   └── llava_agent.py          # LLaVA model wrapper
│
├── tests/
├── requirements.txt
├── Dockerfile
└── README.md

## 🧰 Tech Stack
Component	Technology
Language	Python 3.10+
API	FastAPI
Vision	OpenCV
OCR	Tesseract
VLM	LLaVA
PDF Processing	pdf2image, pdfplumber
Agents	Custom agent framework
Deployment	Uvicorn / Docker

## ⚙️ System Requirements

1️⃣ Python
Python 3.10 or later

2️⃣ Tesseract OCR

Windows

Download: https://github.com/UB-Mannheim/tesseract/wiki

Add installation path to PATH

Linux

sudo apt install tesseract-ocr

3️⃣ Poppler (Required for PDF → Image Conversion)

Poppler is required internally by pdf2image to extract images from PDFs.
This is a runtime dependency, not a project requirement.

Windows

Download:
https://github.com/oschwartz10612/poppler-windows

Extract

Add poppler/bin to PATH

Verify:

pdfinfo -v


Linux

sudo apt install poppler-utils

## 📦 Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/multi_modal_doc_ai.git
cd multi_modal_doc_ai

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac

## 3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Application
uvicorn api.main:app --host 127.0.0.1 --port 8080 --reload


You should see:

## Uvicorn running on http://127.0.0.1:8080

## 🌐 API Usage
Open Swagger UI

👉 http://127.0.0.1:8080/docs

📤 Upload a PDF

Go to /process

Click Try it out

Upload a PDF file

Click Execute

##  📥 Sample Response
{
  "file_name": "sample.pdf",
  "status": "validated",
  "confidence": 0.87,
  "vision_output": {
    "objects_detected": ["table", "diagram"],
    "cv_confidence": 0.88
  },
  "text_output": "Extracted textual content...",
  "fusion_output": {
    "summary": "Combined visual and textual understanding"
  },
  "validation": {
    "agreement_score": 0.9
  }
}

## 📊 Confidence Scoring

Final confidence is calculated using:

confidence = weighted(
    OCR confidence,
    Vision confidence,
    Cross-modal agreement
)


## This ensures multi-modal reliability and supports human-in-the-loop review.

🧪 Supported Document Types

✅ Scanned PDFs

✅ Digital PDFs with images

✅ Technical papers (figures + text)

✅ Forms & reports

## 🧠 Why This Design?

Agent separation improves robustness

Vision + Text fusion avoids hallucinations

Validation agent cross-checks modalities

Confidence scoring supports production use

## 🐳 Docker 
docker build -t multimodal-doc-ai .
docker run -p 8080:8080 multimodal-doc-ai

## 📌 Notes for Evaluators

Poppler is a system dependency, not a framework requirement

Vision agent loads lazily to optimize memory

Architecture supports easy extension to RAG & vector DBs




👨‍💻 Author
Sreeram Venkata Phani Kiranmai 
Applied AI / Multi-Modal Systems
Built for QuickPlans AI – HiDevs Challenge

