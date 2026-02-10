from .search_metrics import hit_rate, precision_at_k
from .answer_metrics import faithfulness

def evaluate(question, retrieved, answer, ground_truth):
    # Search quality metrics
    hr = hit_rate(retrieved, ground_truth)
    pk = precision_at_k(retrieved, ground_truth)

    # Prepare contexts for faithfulness check
    contexts = [doc.page_content for doc in retrieved]
    faith = faithfulness(answer, contexts)

    # Failure attribution
    if hr == 0:
        failure = "retrieval_failure"
    elif faith < 0.5:
        failure = "generation_failure"
    else:
        failure = "pass"

    return {
        "hit_rate": hr,
        "precision@k": pk,
        "faithfulness": faith,
        "failure_reason": failure
    }
