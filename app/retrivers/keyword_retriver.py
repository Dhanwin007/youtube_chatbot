import os
import psycopg

from dotenv import load_dotenv
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document

load_dotenv()

COLLECTION_NAME = "Yt_chatbot"


def keyword_search(query, k=5):

    if not query.strip():
        raise ValueError("Search query cannot be empty.")

    database_url = os.getenv("NEON_DATABASE_URL")

    if not database_url:
        raise ValueError("NEON_DATABASE_URL is missing from .env")

    search_query = """
        SELECT
            e.document,
            e.cmetadata
        FROM langchain_pg_embedding AS e
        JOIN langchain_pg_collection AS c
            ON e.collection_id = c.uuid
        WHERE c.name = %s;
    """

    with psycopg.connect(database_url) as connection:
        rows = connection.execute(
            search_query,
            (COLLECTION_NAME,)
        ).fetchall()

    documents = [
        Document(
            page_content=row[0],
            metadata=row[1] or {}
        )
        for row in rows
    ]

    if not documents:
        return []

    retriever = BM25Retriever.from_documents(
        documents,
        k=k
    )

    return retriever.invoke(query)