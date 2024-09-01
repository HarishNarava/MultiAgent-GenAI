# agents/researcher.py
from api.ares_api import search_ares
from api.youtube_api import search_videos, transcribe_video
from content_extraction.extractor import extract_text, extract_images

def research(task: str) -> Dict:
    # Perform web search
    web_results = search_ares(task)
    
    # Search YouTube
    video_results = search_videos(task)
    
    # Extract content from top results
    extracted_content = []
    for result in web_results[:3]:
        text = extract_text(result['url'])
        images = extract_images(result['url'])
        extracted_content.append({"text": text, "images": images})
    
    # Transcribe top YouTube video
    if video_results:
        transcript = transcribe_video(video_results[0]['id'])
        extracted_content.append({"text": transcript, "source": "youtube"})
    
    # Summarize findings
    summary = generate_text(f"Summarize the following research findings: {extracted_content}")
    
    return {
        "summary": summary,
        "web_results": web_results,
        "video_results": video_results,
        "extracted_content": extracted_content
    }
