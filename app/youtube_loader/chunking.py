
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(combined, video_id, video_url):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""],
        add_start_index=True
    )

    # Create an initial LangChain Document.
    from langchain_core.documents import Document

    source_document = Document(
        page_content=combined["text"],
        metadata={
            "video_id": video_id,
            "source": video_url
        }
    )

    # Split the existing Document into smaller Documents.
    documents = splitter.split_documents([source_document])

    for index, document in enumerate(documents):

        chunk_start = document.metadata["start_index"]
        chunk_end = chunk_start + len(document.page_content)

        overlapping_segments = [
            segment
            for segment in combined["segments"]
            if segment["text_start"] < chunk_end
            and segment["text_end"] > chunk_start
        ]

        if not overlapping_segments:
            raise ValueError(
                "Could not map chunk to transcript timestamps."
            )

        document.metadata.update({
            "chunk_index": index,
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
