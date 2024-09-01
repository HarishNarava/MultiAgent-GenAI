# llm/llm_wrapper.py
import vllm

llm = None

def initialize_llm():
    global llm
    # Initialize local LLM using vllm
    llm = vllm.LLM(model="path/to/your/local/model")

def generate_text(prompt: str) -> str:
    global llm
    if llm is None:
        raise Exception("LLM not initialized")
    
    # Generate text using the local LLM
    result = llm.generate(prompt)
    return result[0].text
