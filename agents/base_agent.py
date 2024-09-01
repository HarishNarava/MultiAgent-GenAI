# agents/base_agent.py
from typing import Callable, Dict
from llm.llm_wrapper import generate_text

def execute_agent_task(agent_function: Callable, task: str) -> Dict:
    try:
        result = agent_function(task)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
