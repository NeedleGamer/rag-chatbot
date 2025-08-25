# app/hello_streamlit.py
import sys, pathlib
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from src.config.settings import settings

st.set_page_config(page_title="RAG Chatbot - Hello")
st.title("RAG Chatbot: environment check")
st.write("LOG_LEVEL:", settings.LOG_LEVEL)
st.write("CHROMA_DIR:", settings.CHROMA_DIR)
st.success("If you can see this in a browser, Streamlit is alive.")
