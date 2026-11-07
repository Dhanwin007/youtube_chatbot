
# app/vectorstore/neon.py

import os

from dotenv import load_dotenv
from langchain_postgres import PGVector

from app.vectorstore.embeddings import get_embedding_model


load_dotenv()

COLLECTION_NAME = "Yt_chatbot"


def get_vector_store():
    """
    Establish the Neon connection and initialize
    the LangChain PGVector vector store.
    """

    database_url = os.getenv("NEON_DATABASE_URL")

    if not database_url:
        raise ValueError("NEON_DATABASE_URL is missing from .env")

    embeddings = get_embedding_model()

    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=COLLECTION_NAME,
        connection=database_url,
        use_jsonb=True
    )

    return vector_store
