# scripts/test_imports.py
import sys
print("python:", sys.version)
for name in [
    "langchain", "chromadb", "streamlit",
    "sentence_transformers", "pydantic",
    "pydantic_settings", "dotenv", "groq"
]:
    __import__(name)
print("all imports OK")
