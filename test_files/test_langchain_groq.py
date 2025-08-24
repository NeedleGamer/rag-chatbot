from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

msg = llm.invoke([("human", "Return the string: ping pong")])
print(msg.content.strip())
