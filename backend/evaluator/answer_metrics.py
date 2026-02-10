from .llm_judge import llm_judge

def faithfulness(answer: str, contexts: list[str]) -> float:
    """
    Checks whether the generated answer is supported by the retrieved contexts.
    """

    prompt = f"""
You are an evaluator.

Answer:
{answer}

Retrieved Contexts:
{contexts}

Is the answer supported by the contexts?
Respond with exactly one of the following:
SUPPORTED
PARTIALLY_SUPPORTED
NOT_SUPPORTED
"""

    verdict = llm_judge(prompt)

    if "SUPPORTED" in verdict:
        return 1.0
    elif "PARTIALLY" in verdict:
        return 0.5
    else:
        return 0.0
