# rate_limit_probe.py
import os, requests, json
from dotenv import load_dotenv
load_dotenv()
h = {"Authorization": f"Bearer {os.environ.get("GROQ_API_KEY")}",
     "Content-Type": "application/json"}
data = {"model":"llama-3.3-70b-versatile",
        "messages":[{"role":"user","content":"ping"}],
        "max_tokens":4}
r = requests.post("https://api.groq.com/openai/v1/chat/completions",
                  headers=h, json=data, timeout=30)
print("Status:", r.status_code)
for k in ["x-ratelimit-limit-requests","x-ratelimit-remaining-requests",
          "x-ratelimit-limit-tokens","x-ratelimit-remaining-tokens","retry-after"]:
    print(k, "=>", r.headers.get(k))
print("Response:", json.dumps(r.json(), indent=2))