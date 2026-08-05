from langchain_openai import ChatOpenAI

from config.settings import LLM_MODEL


def get_llm():

    return ChatOpenAI(
        model=LLM_MODEL,
        temperature=0
    )