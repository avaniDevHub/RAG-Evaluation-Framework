def extract_text(chunk):
    """
    Handles both raw strings and LangChain Document objects.
    """
    if hasattr(chunk, "page_content"):
        return chunk.page_content
    return chunk


def is_relevant(chunk, ground_truth):
    chunk_text = extract_text(chunk).lower()

    for gt in ground_truth:
        if gt.lower() in chunk_text:
            return True

    return False


def hit_rate(retrieved, ground_truth):
    if not retrieved:
        return 0

    return int(any(is_relevant(chunk, ground_truth) for chunk in retrieved))


def precision_at_k(retrieved, ground_truth, k=5):
    retrieved_k = retrieved[:k]

    if not retrieved_k:
        return 0.0

    relevant = sum(
        1 for chunk in retrieved_k
        if is_relevant(chunk, ground_truth)
    )

    return relevant / len(retrieved_k)
