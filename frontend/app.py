# frontend/app.py
import streamlit as st

st.set_page_config(
    page_title="VideoMind AI",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 VideoMind AI")

st.markdown("""
## Features
- Upload Video/Audio
- YouTube Video Processing
- AI Summarization
- AI Chat
- Action Item Extraction
- Decision Extraction
- Question Extraction
""")