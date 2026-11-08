
import os

from dotenv import load_dotenv
from langchain_cohere import CohereRerank
from langchain_core.documents import Document

load_dotenv()


def rerank_documents(query, documents, top_n=5):
    """
    Rerank retrieved documents using Cohere Rerank.
    """

    if not query or not query.strip():
        raise ValueError("Search query cannot be empty.")

    if not documents:
        return []

    api_key = os.getenv("COHERE_API_KEY")

    if not api_key:
        raise ValueError("COHERE_API_KEY missing from .env")

    reranker = CohereRerank(
        cohere_api_key=api_key,
        model="rerank-v4.0-fast",
        top_n=top_n
    )

    reranked_documents = reranker.compress_documents(
        documents=documents,
        query=query
    )

    return reranked_documents
