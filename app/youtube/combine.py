
def format_timestamp(seconds):
    """Convert seconds into HH:MM:SS format."""

    total_seconds = int(seconds)

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def combine_transcript(segments):
    """
    Combine transcript segments into continuous text.

    Preserve the original segments and their timestamps
    for future timestamp-aware chunking.
    """

    combined_parts = []
    current_position = 0

    for segment in segments:
        text = segment["text"].strip()

        if not text:
            continue

        start_position = current_position
        end_position = start_position + len(text)

        combined_parts.append(text)

        segment_info = {
            "text": text,
            "start": segment["start"],
            "duration": segment["duration"],
            "text_start": start_position,
            "text_end": end_position
        }

        current_position = end_position + 1

        # Preserve the processed segment information
        segment_info["separator_after"] = " "

        # Store the segment
        if "processed_segments" not in locals():
            processed_segments = []

        processed_segments.append(segment_info)

    combined_text = " ".join(combined_parts)

    return {
        "text": combined_text,
        "segments": processed_segments if segments else []
    }
