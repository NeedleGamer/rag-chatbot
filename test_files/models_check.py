# models_check.py
import os, requests
from dotenv import load_dotenv
load_dotenv()
assert os.getenv("GROQ_API_KEY"), "GROQ_API_KEY missing. Put it in .env"
print("Env OK")
url = "https://api.groq.com/openai/v1/models"
headers = {"Authorization": f"Bearer {os.getenv("GROQ_API_KEY")}"}
print(requests.get(url, headers=headers, timeout=30).json())
