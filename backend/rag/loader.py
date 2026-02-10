import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_documents():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    docs_path = os.path.join(BASE_DIR, "data", "docs")


    documents = []

    for filename in os.listdir(docs_path):
        if filename.endswith(".txt"):
            loader = TextLoader(
                os.path.join(docs_path, filename),
                encoding="utf-8"
            )
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)
