from langchain.schema.runnable import RunnableLambda

from .loader import load_documents
from .retriever import build_retriever
from .generator import build_generator

# Build pipeline once at startup
documents = load_documents()
retriever = build_retriever(documents)
generator = build_generator()

# LangChain RAG pipeline (Runnable)
rag_chain = (
    RunnableLambda(lambda q: {
        "question": q,
        "documents": retriever.get_relevant_documents(q)
    })
    | generator
)

def run_rag(question: str):
    result = rag_chain.invoke(question)

    retrieved_docs = result["documents"]
    answer = result["answer"]

    return question, retrieved_docs, answer
