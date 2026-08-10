import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

COLLECTION_NAME = "rumor_buster"

QDRANT_PATH = "./qdrant_db"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "gpt-4o-mini"

PDF_FILE = "data/whitepaper.pdf"
CSV_FILE = "data/internal_logs.csv"
JSON_FILE = "data/social_posts.json"