
from app.vectorstore.chroma import get_vector_store


def ingest_documents(documents, video_id):
    """
    Store transcript documents and their embeddings in ChromaDB.
    """

    if not documents:
        raise ValueError("No documents provided for ingestion.")

    vector_store = get_vector_store()

    ids = [
        f"{video_id}_{index}"
        for index in range(len(documents))
    ]

    # Delete previously ingested chunks for this video.
    vector_store.delete(ids=ids)

    # Add globally unique document IDs to metadata.
    for index, document in enumerate(documents):
        document.metadata["document_id"] = ids[index]

    # Store documents and generate embeddings.
    vector_store.add_documents(
        documents=documents,
        ids=ids
    )

    return len(documents)
