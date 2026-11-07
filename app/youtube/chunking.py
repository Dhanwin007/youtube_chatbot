from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(combined, video_id, video_url):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""],
        add_start_index=True
    )

    documents = splitter.create_documents(
        texts=[combined["text"]],
        metadatas=[{
            "video_id": video_id,
            "source": video_url
        }]
    )

    # Map each chunk to its original transcript timestamps
    for document in documents:

        chunk_start = document.metadata["start_index"]
        chunk_end = chunk_start + len(document.page_content)

        overlapping_segments = [
            segment
            for segment in combined["segments"]
            if (
                segment["text_start"] < chunk_end
                and segment["text_end"] > chunk_start
            )
        ]

        if not overlapping_segments:
            raise ValueError(
                "Could not map a chunk to its transcript timestamps."
            )

        document.metadata.update({
            "start": min(
                segment["start"]
                for segment in overlapping_segments
            ),
            "end": max(
                segment["start"] + segment["duration"]
                for segment in overlapping_segments
            ),
            "end_index": chunk_end
        })

    return documents