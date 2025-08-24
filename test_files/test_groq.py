import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_groq_api():
    """
    Tests the connection to the Groq API with a simple chat completion.
    """
    try:
        # Get the API key from environment variables
        api_key = os.getenv("GROQ_API_KEY")
        groq_model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        if not api_key:
            print("Error: GROQ_API_KEY not found. Please set it in your .env file.")
            return

        # Initialize the ChatGroq model
        chat = ChatGroq(temperature=0, groq_api_key=api_key, model_name=groq_model)

        # Create a message and invoke the model
        message = HumanMessage(content="Explain the importance of low latency LLMs.")
        response = chat.invoke([message])

        # Print the response content
        print("Successfully connected to Groq API!")
        print("Response:", response.content)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_groq_api()