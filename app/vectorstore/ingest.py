
# app/vectorstore/ingest.py

from app.vectorstore.neon import get_vector_store


def ingest_documents(documents, video_id):
    """
    Store transcript documents and their embeddings in Neon.
    """

    if not documents:
        raise ValueError("No documents provided for ingestion.")

    vector_store = get_vector_store()

    ids = [
        f"{video_id}_{index}"
        for index in range(len(documents))
    ]

    # Replace previously ingested chunks for this video.
    # PGVector uses these IDs to identify the inserted documents.
    vector_store.delete(ids=ids)

    vector_store.add_documents(
        documents=documents,
        ids=ids
    )

    return len(documents)
