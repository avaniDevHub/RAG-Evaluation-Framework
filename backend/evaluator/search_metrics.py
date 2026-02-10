def hit_rate(retrieved, ground_truth):
    return int(any(gt in chunk for gt in ground_truth for chunk in retrieved))

def precision_at_k(retrieved, ground_truth, k=5):
    retrieved_k = retrieved[:k]
    relevant = sum(
        1 for chunk in retrieved_k
        if any(gt in chunk for gt in ground_truth)
    )
    return relevant / k
