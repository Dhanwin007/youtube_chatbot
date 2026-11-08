
from langchain_classic.retrievers.ensemble import EnsembleRetriever
from langchain_core.retrievers import BaseRetriever

from app.retrivers.semantic_retriver import retrieve_documents
from app.retrivers.keyword_retriver import keyword_search


class SemanticRetriever(BaseRetriever):

    def _get_relevant_documents(self, query, *, run_manager):
        return retrieve_documents(query)


class KeywordRetriever(BaseRetriever):

    def _get_relevant_documents(self, query, *, run_manager):
        return keyword_search(query)


def hybrid_search(query, k=5):

    if not query or not query.strip():
        raise ValueError("Search query cannot be empty.")

    semantic_retriever = SemanticRetriever()
    keyword_retriever = KeywordRetriever()

    ensemble_retriever = EnsembleRetriever(
        retrievers=[
            semantic_retriever,
            keyword_retriever
        ],
        weights=[0.5, 0.5],
        id_key="chunk_index"
    )

    return ensemble_retriever.invoke(query)[:k]
