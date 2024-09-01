# content_extraction/extractor.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_text(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    
    # Get text
    text = soup.get_text()
    
    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    return text

def extract_images(url: str) -> List[str]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    images = []
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            images.append(img_url)
    
    return images
