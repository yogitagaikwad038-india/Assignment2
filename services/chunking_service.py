from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_pdf_documents(pdf_docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(pdf_docs)

    return chunks


def chunk_record_documents(docs):

    return docs