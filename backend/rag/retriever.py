from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def build_retriever(documents):
    """
    Builds a FAISS-based retriever from document chunks.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(documents, embeddings)

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )

    return retriever
