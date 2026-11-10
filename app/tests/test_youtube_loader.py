
from app.youtube_loader.transcript import load_transcript
from app.youtube_loader.combine import combine_transcript
from app.youtube_loader.chunking import create_chunks


video_url = input("Enter YouTube URL: ").strip()


# 1. Load transcript Documents
transcript_documents = load_transcript(video_url)

print("\nTranscript loaded:", len(transcript_documents))
print("Document type:", type(transcript_documents[0]))
print("First document:", transcript_documents[0])


# 2. Extract video ID from loader metadata
video_id = transcript_documents[0].metadata.get("video_id")

if not video_id:
    from langchain_community.document_loaders import YoutubeLoader

    video_id = YoutubeLoader.extract_video_id(video_url)

print("\nVideo ID:", video_id)


# 3. Combine transcript
combined = combine_transcript(transcript_documents)

print("\nCombined transcript length:", len(combined["text"]))
print("Transcript segments:", len(combined["segments"]))


# 4. Create chunks
chunk_documents = create_chunks(
    combined,
    video_id,
    video_url
)

print("\nTotal chunks:", len(chunk_documents))


# 5. Inspect results
for document in chunk_documents[:3]:

    print("\n-----------------------------")
    print("Document type:", type(document))
    print("Chunk:", document.metadata["chunk_index"])
    print("Start:", document.metadata["start"])
    print("End:", document.metadata["end"])
    print("Content:", document.page_content[:250])
    print("Metadata:", document.metadata)
