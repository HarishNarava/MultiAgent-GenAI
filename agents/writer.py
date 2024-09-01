# agents/writer.py
from llm.llm_wrapper import generate_text

def write(task: str) -> Dict:
    # Generate an outline
    outline = generate_text(f"Create an outline for: {task}")
    
    # Generate content for each section
    content = {}
    for section in outline.split('\n'):
        if section.strip():
            content[section] = generate_text(f"Write content for the section: {section}")
    
    # Generate a conclusion
    conclusion = generate_text(f"Write a conclusion for: {task}")
    
    return {
        "summary": "Written content generated",
        "outline": outline,
        "content": content,
        "conclusion": conclusion
    }
