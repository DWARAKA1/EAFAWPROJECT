from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

def test_finance_analysis():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("GROQ_API_KEY not found")
        return
    
    try:
        llm = ChatGroq(
            temperature=0,
            groq_api_key=api_key,
            model_name="llama-3.1-8b-instant"
        )
        
        prompt = """
        You are a Senior Financial Analyst. Analyze this financial data:
        - Company: Sample Corp
        - Revenue: $1,000,000
        - Expenses: $800,000
        - Assets: $2,000,000
        - Liabilities: $500,000
        
        Provide key insights and recommendations.
        """
        
        response = llm.invoke(prompt)
        print("Financial Analysis Results:")
        print("=" * 50)
        print(response.content)
        print("=" * 50)
        print("SUCCESS: Finance analysis completed!")
        
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_finance_analysis()