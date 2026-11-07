# #video_url = "https://www.youtube.com/watch?v=376Ay_Lv-9o"


from app.youtube.transcript import (
    extract_transcript,
    extract_video_id
)
from app.youtube.combine import combine_transcript
from app.youtube.chunking import create_chunks
from app.youtube.combine import format_timestamp


video_url = "https://www.youtube.com/watch?v=376Ay_Lv-9o"

# 1. Extract transcript
video_id = extract_video_id(video_url)
segments = extract_transcript(video_url)

# 2. Combine transcript
combined = combine_transcript(segments)

# 3. Create chunks
documents = create_chunks(
    combined,
    video_id,
    video_url
)

# 4. Inspect the results
print("Total transcript segments:", len(segments))
print("Total chunks:", len(documents))

for index, document in enumerate(documents[:5]):

    print(f"\n========== CHUNK {index + 1} ==========")

    print("Content:")
    print(document.page_content)

    print("\nMetadata:")
    print("Video ID:", document.metadata["video_id"])
    print("Source:", document.metadata["source"])
    print(
        "Timestamp:",
        format_timestamp(document.metadata["start"]),
        "-",
        format_timestamp(document.metadata["end"])
    )
    print("Start index:", document.metadata["start_index"])
    print("End index:", document.metadata["end_index"])




