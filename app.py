from rich import print

from langchain_openai import ChatOpenAI

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from config.settings import *

from utils.logger import get_logger

from loaders.pdf_loader import load_pdf

from loaders.csv_loader import load_csv

from loaders.json_loader import load_json

from services.embedding_service import (
    get_embeddings
)

from services.vector_service import (
    create_vector_store
)

from services.fact_checker_service import (
    analyze_claim
)
from services.chunking_service import (
    chunk_pdf_documents,
    chunk_record_documents
)

logger = get_logger()

logger.info(
    "[STARTUP] Application Started"
)

print("""
╔══════════════════════════════════════════════════════════╗
║       AI FAKE NEWS & RUMOR BUSTER (Enterprise)          ║
║     PDF + CSV + JSON Cross Verification System          ║
╚══════════════════════════════════════════════════════════╝
""")

print(
    "\nINFO --- [NODE] DOCUMENT INGESTION ---"
)

print("\nLoading PDF...")
pdf_docs = load_pdf("data/whitepaper.pdf")

print("Loading CSV...")
csv_docs = load_csv("data/internal_logs.csv")

print("Loading JSON...")
json_docs = load_json("data/social_posts.json")


all_docs = pdf_docs + csv_docs + json_docs

print("\n======== DOCUMENT SUMMARY ========")

print(f"PDF Pages    : {len(pdf_docs)}")
print(f"CSV Records  : {len(csv_docs)}")
print(f"JSON Records : {len(json_docs)}")

print(
    f"Total Documents Loaded: {len(all_docs)}"
)

print(
    "\nINFO --- [NODE] SMART CHUNKING ---"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(
    all_docs
)

pdf_chunks = chunk_pdf_documents(pdf_docs)
csv_chunks = chunk_record_documents(csv_docs)
json_chunks = chunk_record_documents(json_docs)

all_chunks = pdf_chunks + csv_chunks + json_chunks

print(
    f"Total Chunks Created: {len(chunks)}"
)

print("\nINFO --- [NODE] METADATA TAGGING ---")

for chunk in all_chunks[:5]:

    print("\nChunk Content:")
    print(chunk.page_content[:100])

    print("Metadata:")

    print(chunk.metadata)

print(
    "\nINFO --- [NODE] EMBEDDING SERVICE ---"
)

embeddings = get_embeddings()

print(
    "Embeddings Model Loaded"
)

print(
    "\nINFO --- [NODE] VECTOR STORAGE ---"
)

vector_db = create_vector_store(
    chunks,
    embeddings
)

print(
    "FAISS Index Created"
)

print(
    "\nINFO --- [NODE] VECTOR HEALTH CHECK ---"
)

health = vector_db.similarity_search_with_score(
    "Project Titan budget",
    k=3
)

print(
    f"Chunk Count: {len(chunks)}"
)

for doc, score in health:

    print(
        f"Search Score: {score}"
    )

query = input(
    "\nEnter Rumor To Investigate:\n> "
)

print(
    "\nINFO --- [NODE] FILTERED SEARCH ---"
)

official_docs = [
    d for d in chunks
    if d.metadata["source_type"]
    == "Official"
]

rumor_docs = [
    d for d in chunks
    if d.metadata["source_type"]
    == "Rumor"
]

official_context = "\n".join(
    [
        d.page_content
        for d in official_docs
    ]
)

rumor_context = "\n".join(
    [
        d.page_content
        for d in rumor_docs
    ]
)

context = f"""
OFFICIAL SOURCES

{official_context}

SOCIAL MEDIA SOURCES

{rumor_context}
"""

print(
    "\nINFO --- [NODE] OPENAI ANALYSIS ---"
)

llm = ChatOpenAI(
    model=LLM_MODEL,
    temperature=0
)

output = analyze_claim(
    llm,
    context,
    query
)

print()
print("=" * 60)
print("FACT CHECK REPORT")
print("=" * 60)
print(output)

print("\nSANITY TESTS")

tests = [
    "Was Project Titan cancelled?",
    "Is budget approval active?",
    "Did social media claim cancellation?"
]

for test in tests:

    result = analyze_claim(
        llm,
        context,
        test
    )

    print(f"\nPASS -> {test}")