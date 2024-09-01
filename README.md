# Multi-Agent System for General-Purpose Tasks

This project implements a multi-agent system capable of executing a wide range of user requests using local or quantized LLMs and various APIs and tools.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up environment variables:
   - ARES_API_KEY: Your ARES API key
   - YOUTUBE_API_KEY: Your YouTube API key
6. Place your local LLM model in the appropriate directory and update the path in `llm/llm_wrapper.py`

## Usage

1. Run the FastAPI server: `uvicorn main:app --reload`
2. Access the Streamlit UI: `streamlit run ui/streamlit_app.py`
3. Enter your task in the UI and click "Process Task"

## Project Structure

- `main.py`: Entry point of the application
- `agents/`: Contains agent implementations and manager
- `llm/`: LLM wrapper and related utilities
- `api/`: API integrations (ARES, YouTube)
- `content_extraction/`: Modules for extracting content from various sources
- `ui/`: Streamlit user interface
