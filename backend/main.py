from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import json

load_dotenv()

from fastapi import FastAPI
from schemas import EvaluateRequest
from rag.pipeline import run_rag
from evaluator.judge import evaluate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Safe path resolution
BASE_DIR = os.path.dirname(__file__)
with open(os.path.join(BASE_DIR, "data", "ground_truth.json")) as f:
    GROUND_TRUTH = {
        d["question"]: d["relevant_chunks"]
        for d in json.load(f)
    }

@app.post("/evaluate")
def evaluate_rag(req: EvaluateRequest):
    question, retrieved, answer = run_rag(req.question)

    metrics = evaluate(
        question,
        retrieved,
        answer,
        GROUND_TRUTH.get(question, [])
    )

    # 🔴 IMPORTANT FIX: serialize LangChain Documents
    retrieved_chunks = [
        {
            "content": doc.page_content,
            "metadata": doc.metadata
        }
        for doc in retrieved
    ]

    return {
        "question": question,
        "retrieved_chunks": retrieved_chunks,
        "answer": answer,
        "metrics": metrics
    }
