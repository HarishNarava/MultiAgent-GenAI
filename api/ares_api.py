# api/ares_api.py
import requests

ARES_API_KEY = "your_ares_api_key_here"
ARES_BASE_URL = "https://api.traversaal.ai"

def search_ares(query: str) -> List[Dict]:
    headers = {
        "Authorization": f"Bearer {ARES_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"query": query}
    response = requests.post(f"{ARES_BASE_URL}/search", json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["results"]
