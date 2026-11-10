
def combine_transcript(documents):
    """
    Combine transcript Documents into continuous text.
    Preserve timestamp metadata and character offsets.
    """

    combined_parts = []
    processed_segments = []

    current_position = 0

    for document in documents:

        text = document.page_content.strip()

        if not text:
            continue

        start_position = current_position
        end_position = start_position + len(text)

        combined_parts.append(text)

        processed_segments.append({
            "text": text,
            "start": document.metadata["start"],
            "duration": document.metadata["duration"],
            "text_start": start_position,
            "text_end": end_position
        })

        current_position = end_position + 1

    return {
        "text": " ".join(combined_parts),
        "segments": processed_segments
    }
