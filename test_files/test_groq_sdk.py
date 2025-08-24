from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

resp = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "something funny."}],
    max_tokens=5,
)
print(resp.choices[0].message.content.strip())
#assert resp.choices[0].message.content.strip() == "pong"