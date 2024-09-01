# agents/analyzer.py
from llm.llm_wrapper import generate_text

def analyze(task: str) -> Dict:
    # Generate analysis points
    analysis_points = generate_text(f"Provide key analysis points for: {task}")
    
    # Evaluate strengths and weaknesses
    strengths = generate_text(f"List strengths related to: {task}")
    weaknesses = generate_text(f"List weaknesses related to: {task}")
    
    # Generate recommendations
    recommendations = generate_text(f"Provide recommendations based on the analysis of: {task}")
    
    return {
        "summary": "Analysis completed",
        "analysis_points": analysis_points,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations
    }
