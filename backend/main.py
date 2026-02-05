from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import EvaluationRequest
from evaluator.search_metrics import hit_rate, precision_at_k
from evaluator.answer_metrics import (
    faithfulness_score,
    relevance_score,
    completeness_score
)

app = FastAPI(title="RAG Evaluation Framework")

# ✅ CORS FIX (THIS IS CRITICAL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/evaluate")
def evaluate(payload: EvaluationRequest):
    hit = hit_rate(payload.search_results)
    precision = precision_at_k(payload.search_results)

    context = " ".join([doc.content for doc in payload.search_results])

    return {
        "search_quality": {
            "hit_rate": hit,
            "precision@5": precision
        },
        "answer_quality": {
            "faithfulness": faithfulness_score(context, payload.answer),
            "relevance": relevance_score(payload.question, payload.answer),
            "completeness": completeness_score(context, payload.answer)
        }
    }
