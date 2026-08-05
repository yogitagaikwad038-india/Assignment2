import pandas as pd

from langchain_core.documents import Document


def load_csv(path):

    df = pd.read_csv(path)

    documents = []

    for _, row in df.iterrows():

        documents.append(
            Document(
                page_content=str(row.to_dict()),
                metadata={
                    "source_type": "Official",
                    "date": "2026-08-02"
                }
            )
        )

    return documents