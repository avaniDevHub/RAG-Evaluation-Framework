from pydantic import BaseModel
from typing import List

class SearchResult(BaseModel):
    document_id: str
    content: str
    relevant: bool

class EvaluateRequest(BaseModel):
    question: str
