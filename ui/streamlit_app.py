# ui/streamlit_app.py
import streamlit as st
from agents.agent_manager import process_task

def launch_ui():
    st.title("Multi-Agent System for General-Purpose Tasks")
    task = st.text_input("Enter your task:")
    if st.button("Process Task"):
        with st.spinner("Processing..."):
            result = process_task(task)
        
        st.subheader("Result Summary")
        st.write(result["summary"])
        
        st.subheader("Detailed Results")
        for key, value in result["details"].items():
            st.write(f"**{key.capitalize()}**")
            st.json(value)

if __name__ == "__main__":
    launch_ui()
