from langchain_openai import ChatOpenAI

from config.settings import (
    OPENAI_API_KEY,
    LLM_MODEL
)


def get_llm():

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY not found in .env file"
        )

    return ChatOpenAI(
        api_key=OPENAI_API_KEY,
        model=LLM_MODEL,
        temperature=0
    )