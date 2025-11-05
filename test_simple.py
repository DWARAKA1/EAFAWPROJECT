from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

def test_groq():
    api_key = os.getenv("GROQ_API_KEY")
    print(f"API Key loaded: {'Yes' if api_key else 'No'}")
    
    if api_key:
        try:
            llm = ChatGroq(
                temperature=0,
                groq_api_key=api_key,
                model_name="llama3-8b-8192"
            )
            
            response = llm.invoke("What is 2+2?")
            print(f"Groq Response: {response.content}")
            return True
        except Exception as e:
            print(f"Groq Error: {e}")
            return False
    return False

if __name__ == "__main__":
    test_groq()