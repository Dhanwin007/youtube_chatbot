
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document

from app.vectorstore.chroma import get_vector_store


def keyword_search(query, k=5):
    """
    Perform keyword-based retrieval using BM25Retriever
    with documents stored in ChromaDB.
    """

    if not query or not query.strip():
        raise ValueError("Search query cannot be empty.")

    # 1. Initialize Chroma vector store
    vector_store = get_vector_store()

    # 2. Fetch all stored documents from Chroma
    stored_data = vector_store.get()

    documents = [
        Document(
            page_content=content,
            metadata=metadata or {}
        )
        for content, metadata in zip(
            stored_data["documents"],
            stored_data["metadatas"]
        )
        if content
    ]

    if not documents:
        return []

    # 3. Build BM25 retriever
    retriever = BM25Retriever.from_documents(
        documents,
        k=k
    )

    # 4. Retrieve keyword-relevant documents
    results = retriever.invoke(query)

    return results
