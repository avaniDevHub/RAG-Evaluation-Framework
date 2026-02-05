from pydantic import BaseModel
from typing import List

class SearchResult(BaseModel):
    document_id: str
    content: str
    relevant: bool

class EvaluationRequest(BaseModel):
    question: str
    search_results: List[SearchResult]
    answer: str
