def llm_judge(prompt: str) -> str:
    """
    Mock LLM judge used for offline evaluation.
    This can be replaced with OpenAI or a local LLM later.
    """

    prompt_lower = prompt.lower()

    # Simple heuristic rules
    if "not supported" in prompt_lower:
        return "NOT_SUPPORTED"

    if "retrieved contexts" in prompt_lower and "answer" in prompt_lower:
        return "SUPPORTED"

    return "PARTIALLY_SUPPORTED"
