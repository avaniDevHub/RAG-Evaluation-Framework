from langchain.schema.runnable import RunnableLambda

def build_generator():
    """
    Mock generator implemented as a LangChain Runnable.
    No OpenAI / no external API calls.
    """

    def generate(inputs):
        question = inputs["question"]
        documents = inputs["documents"]

        if documents:
            answer = (
                "Retrieval Augmented Generation (RAG) retrieves relevant documents "
                "and uses them as context to answer a question. "
                f"This answer is based on retrieved content related to: '{question}'."
            )
        else:
            answer = "No relevant documents were retrieved to answer the question."

        return {
            "answer": answer,
            "documents": documents
        }

    return RunnableLambda(generate)
