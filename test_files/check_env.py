from dotenv import load_dotenv
import os
load_dotenv()
assert os.getenv("GROQ_API_KEY"), "GROQ_API_KEY missing. Put it in .env"
print("Env OK")
print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY")[:4] + "..." + os.getenv("GROQ_API_KEY")[-4:])