
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(video_url: str) -> str:
    """
    Extract the YouTube video ID from a YouTube URL.
    Supports watch, youtu.be and Shorts URLs.
    """

    parsed_url = urlparse(video_url)
    hostname = parsed_url.hostname

    if hostname in ("www.youtube.com", "youtube.com", "m.youtube.com"):
        if parsed_url.path == "/watch":
            video_id = parse_qs(parsed_url.query).get("v", [None])[0]

        elif parsed_url.path.startswith("/shorts/"):
            video_id = parsed_url.path.split("/")[2]

        else:
            video_id = None

    elif hostname == "youtu.be":
        video_id = parsed_url.path.lstrip("/").split("/")[0]

    else:
        video_id = None

    if not video_id:
        raise ValueError("Invalid YouTube URL")

    return video_id


def extract_transcript(video_url: str):
    """
    Extract transcript segments from a YouTube URL.
    """

    video_id = extract_video_id(video_url)

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)

    segments = []

    for snippet in transcript:
        segments.append({
            "text": snippet.text,
            "start": snippet.start,
            "duration": snippet.duration
        })

    return segments
