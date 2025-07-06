# AI Medical Text Classifier API — FastAPI + Transformers

A production-ready **FastAPI** backend that uses a **transformer-based model (Hugging Face)** to classify medical-related text such as symptoms, diagnoses, or patient feedback.

This project demonstrates how to integrate **LLM inference into a web API**, making it useful for healthcare startups, clinical assistants, and real-time triaging systems.

---

## Features

- Real-time text classification using `distilbert-base-uncased-finetuned-sst-2-english`
- FastAPI backend with auto-generated Swagger docs
- Inference pipeline with Hugging Face Transformers
- Packaged with `venv` and clean `.gitignore`
- Live reload using Uvicorn for fast dev

---

## Tech Stack

| Layer       | Technology                              |
|------------|------------------------------------------|
| Backend     | FastAPI                                 |
| ML Pipeline | Hugging Face Transformers (DistilBERT)  |
| Model       | `distilbert-base-uncased-finetuned-sst-2-english` |
| Runtime     | Python 3.10+                            |
| Server      | Uvicorn                                 |

---

## Setup Instructions

```bash
# 1. Clone this repo
git clone https://github.com/YOUR_USERNAME/ai-medical-api.git
cd ai-medical-api

# 2. Create virtual env
python -m venv venv
venv\Scripts\activate     # or source venv/bin/activate on Linux/macOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run API
uvicorn app:app --reload

 API Documentation
Once running, visit:
http://127.0.0.1:8000/docs for Swagger UI.

/classify [POST]
Classifies any input medical sentence.

Request Body:

json
Copy
Edit
{
  "text": "Patient has severe abdominal pain and nausea."
}
Response:

json
Copy
Edit
{
  "label": "POSITIVE",
  "score": 0.9998
}
Use Cases
 Smart triaging of patient symptoms

 Clinical chatbot backend

 Real-time feedback classification for hospitals

 Research assistant for healthcare NLP

Folder Structure
bash
Copy
Edit
.
├── app.py                 # Main FastAPI app
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
├── .gitignore             # Ignored files
└── venv/                  # Virtual environment (excluded)
 Next Improvements
Fine-tune model on clinical datasets (e.g. MIMIC-III)

Add sentiment/multi-label support

Integrate LangChain for context retrieval

Deploy on Hugging Face Spaces or Azure App Service

 Author
Saba Zehra Syed
Data Scientist | MSc DS & Analytics (UK) | AI in Healthcare
 LinkedIn
sabazehrasyed01@gmail.com

