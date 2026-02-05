from .judge import llm_judge

def faithfulness_score(context, answer):
    return llm_judge("faithfulness")

def relevance_score(question, answer):
    return llm_judge("relevance")

def completeness_score(context, answer):
    return llm_judge("completeness")
