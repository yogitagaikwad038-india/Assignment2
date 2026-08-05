import json

from langchain_core.documents import Document


def load_json(path):

    with open(path) as f:

        posts = json.load(f)

    docs = []

    for post in posts:

        docs.append(
            Document(
                page_content=str(post),
                metadata={
                    "source_type": "Rumor",
                    "date": "2026-08-03"
                }
            )
        )

    return docs