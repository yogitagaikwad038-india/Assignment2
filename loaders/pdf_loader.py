from langchain_community.document_loaders import PyPDFLoader


def load_pdf(path):

    loader = PyPDFLoader(path)

    docs = loader.load()

    for doc in docs:

        doc.metadata["source_type"] = "Official"

        doc.metadata["date"] = "2026-08-01"

    return docs