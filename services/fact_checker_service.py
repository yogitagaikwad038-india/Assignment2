from prompts.fact_check_prompt import (
    FACT_PROMPT
)


def analyze_claim(
    llm,
    context,
    question
):

    prompt = FACT_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(
        prompt
    )

    return response.content