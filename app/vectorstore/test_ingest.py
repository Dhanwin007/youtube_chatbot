from app.youtube.transcript import extract_video_id, extract_transcript
from app.youtube.combine import combine_transcript
from app.youtube.chunking import create_chunks

from app.vectorstore.ingest import store_documents
from app.vectorstore.chroma import get_vector_store


video_url = "https://www.youtube.com/watch?v=376Ay_Lv-9o"

# 1. Extract video ID
video_id = extract_video_id(video_url)

# 2. Extract transcript
segments = extract_transcript(video_url)

# 3. Combine transcript segments
combined = combine_transcript(segments)

# 4. Create timestamp-aware chunks
documents = create_chunks(
    combined,
    video_id,
    video_url
)

# Add chunk index to metadata
for index, document in enumerate(documents):
    document.metadata["chunk_index"] = index

# 5. Store documents in Chroma
store_documents(documents, video_id)

# 6. Verify collection count
vector_store = get_vector_store()

print("Total records:", vector_store._collection.count())