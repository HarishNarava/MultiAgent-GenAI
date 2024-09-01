# agents/agent_manager.py
from typing import List, Dict
from .base_agent import execute_agent_task
from .researcher import research
from .writer import write
from .analyzer import analyze

def process_task(task: str) -> Dict:
    # Parse the task and determine which agents to use
    agents_to_use = determine_agents(task)
    
    results = {}
    for agent in agents_to_use:
        if agent == "researcher":
            results["research"] = execute_agent_task(research, task)
        elif agent == "writer":
            results["write"] = execute_agent_task(write, task)
        elif agent == "analyzer":
            results["analyze"] = execute_agent_task(analyze, task)
    
    # Combine and format results
    final_result = combine_results(results)
    return final_result

def determine_agents(task: str) -> List[str]:
    # Logic to determine which agents to use based on the task
    agents = []
    if "research" in task.lower() or "find" in task.lower():
        agents.append("researcher")
    if "write" in task.lower() or "create" in task.lower():
        agents.append("writer")
    if "analyze" in task.lower() or "evaluate" in task.lower():
        agents.append("analyzer")
    return agents

def combine_results(results: Dict) -> Dict:
    # Logic to combine results from different agents
    combined = {
        "summary": "",
        "details": results
    }
    for key, value in results.items():
        combined["summary"] += f"{key.capitalize()}: {value['summary']}\n"
    return combined
