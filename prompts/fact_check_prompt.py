from langchain_core.prompts import PromptTemplate


FACT_PROMPT = PromptTemplate(
    input_variables=[
        "context",
        "question"
    ],

    template="""
You are an AI fact-checking investigator.

Compare all provided sources.

Determine:

1. Verified Facts
2. Unsupported Claims
3. Contradictions
4. Final Verdict
5. Confidence Score

Context:

{context}

Question:

{question}
"""
)