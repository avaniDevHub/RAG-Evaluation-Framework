def hit_rate(search_results):
    for doc in search_results:
        if doc.relevant:
            return 1
    return 0

def precision_at_k(search_results, k=5):
    top_k = search_results[:k]
    if not top_k:
        return 0
    relevant = sum(1 for doc in top_k if doc.relevant)
    return (relevant / len(top_k)) * 100
