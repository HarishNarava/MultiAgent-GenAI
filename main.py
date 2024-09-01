# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from agents.agent_manager import process_task
from llm.llm_wrapper import initialize_llm, generate_text
from api.ares_api import search_ares
from api.youtube_api import search_videos, transcribe_video
from content_extraction.extractor import extract_text, extract_images
import streamlit as st

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

@app.post("/process_task")
async def api_process_task(request: TaskRequest):
    result = process_task(request.task)
    return {"result": result}

@app.on_event("startup")
async def startup_event():
    initialize_llm()

def main():
    st.title("Multi-Agent System for General-Purpose Tasks")
    task = st.text_input("Enter your task:")
    if st.button("Process Task"):
        result = process_task(task)
        st.write(result)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
