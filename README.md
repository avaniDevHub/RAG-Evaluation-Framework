# RAG Evaluation Framework

This project is an end-to-end **Retrieval-Augmented Generation (RAG) Evaluation Framework** that automatically evaluates a RAG pipeline using retrieval and generation quality metrics.  
It combines **LangChain-based RAG**, **FAISS retrieval**, **LLM-based generation**, and **custom evaluation metrics**, exposed through a **FastAPI backend** and an **interactive React dashboard**.

---

## Key Features

- End-to-end RAG pipeline (Retrieval → Generation → Evaluation)
- FAISS-based dense retrieval using sentence embeddings
- LangChain-powered RAG generation
- Automatic evaluation with:
  - Hit Rate
  - Precision@k
  - Faithfulness
- Failure attribution (retrieval failure vs generation failure)
- Ground-truth based evaluation dataset
- Interactive frontend dashboard for single-question evaluation

---

## Project Architecture

```
RAG Model/
├── backend/
│   ├── data/
│   │   ├── docs/                     # Knowledge base documents
│   │   └── ground_truth.json          # Evaluation dataset
│   │
│   ├── rag/
│   │   ├── loader.py                 # Document loading & chunking
│   │   ├── retriever.py              # FAISS-based retriever
│   │   ├── generator.py              # LangChain RAG generator
│   │   └── pipeline.py               # End-to-end RAG pipeline
│   │
│   ├── evaluator/
│   │   ├── search_metrics.py         # Hit Rate, Precision@k
│   │   ├── answer_metrics.py         # Faithfulness scoring
│   │   ├── llm_judge.py              # LLM-based evaluation logic
│   │   └── judge.py                  # Metric aggregation & failure diagnosis
│   │
│   ├── schemas.py                    # Request/response schemas
│   ├── main.py                       # FastAPI application
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ScoreCard.jsx
│   │   │   ├── ContextViewer.jsx
│   │   │   └── FailureBadge.jsx
│   │   ├── pages/
│   │   │   └── Dashboard.jsx
│   │   ├── api.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## How the Evaluation Works

1. User enters a question in the frontend dashboard.
2. The FastAPI backend triggers the RAG pipeline:
   - Documents are retrieved using FAISS.
   - Retrieved contexts are passed to the LLM for answer generation.
3. The evaluator compares retrieved contexts with ground truth.
4. Metrics are computed:
   - **Hit Rate** – checks if any relevant chunk is retrieved.
   - **Precision@k** – measures relevance among top-k retrieved chunks.
   - **Faithfulness** – evaluates whether the answer is grounded in retrieved content.
5. The system assigns a failure type:
   - `retrieval_failure`
   - `generation_failure`
   - `pass`
6. Results are returned to the frontend and visualized.

---

## Evaluation Dataset

The evaluation uses a **ground truth dataset** stored in:

```
backend/data/ground_truth.json
```

Example:
```json
[
  {
    "question": "What is Retrieval Augmented Generation?",
    "relevant_chunks": [
      "Retrieval Augmented Generation (RAG) is a technique that enhances large language models"
    ]
  },
  {
    "question": "What does precision@k measure?",
    "relevant_chunks": [
      "Precision@k measures how many of the top k retrieved documents are relevant."
    ]
  }
]
```

This dataset enables objective evaluation of retriever quality.

---

## Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend will run at:
```
http://127.0.0.1:8000
```

Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at:
```
http://localhost:5173
```

---

## Current Scope

- Single-question evaluation through UI
- Automatic end-to-end RAG evaluation
- Metric-based failure diagnosis
- Dataset-backed retrieval evaluation

---

## Planned Improvements

- Batch evaluation over multiple questions
- Per-document recall metrics
- Retriever ranking diagnostics
- Visualization of metric trends
- Support for multiple retrievers and LLMs

---

## Why This Project Matters

Unlike simple metric calculators, this framework:
- Evaluates the **entire RAG pipeline**, not isolated components
- Diagnoses whether failures originate from retrieval or generation
- Aligns with how real-world RAG systems are evaluated in research and industry


