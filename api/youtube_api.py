# api/youtube_api.py
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build

YOUTUBE_API_KEY = "your_youtube_api_key_here"

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def search_videos(query: str) -> List[Dict]:
    request = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=5
    )
    response = request.execute()
    return [
        {
            "id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"]
        }
        for item in response["items"]
    ]

def transcribe_video(video_id: str) -> str:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript])
    except Exception as e:
        print(f"Error transcribing video {video_id}: {str(e)}")
        return ""
