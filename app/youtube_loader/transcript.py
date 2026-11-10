
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders.youtube import TranscriptFormat


def load_transcript(video_url: str):
    """
    Load YouTube transcript as LangChain Documents.
    Each document represents a transcript line with timestamp metadata.
    """

    loader = YoutubeLoader.from_youtube_url(
        video_url,
        language=["en"],
        transcript_format=TranscriptFormat.LINES,
        add_video_info=False
    )

    documents = loader.load()

    if not documents:
        raise ValueError("No transcript available for this video.")

    return documents
