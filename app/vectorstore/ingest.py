from app.vectorstore.chroma import get_vector_store


def store_documents(documents, video_id):

    vector_store = get_vector_store()

    ids = [
        f"{video_id}_{index}"
        for index in range(len(documents))
    ]

    vector_store.add_documents(
        documents=documents,
        ids=ids
    )

    print(f"Successfully stored {len(documents)} chunks.")

    return ids