from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    ALLOWED_MODEL_NAMES = [
        "mixtral-8x7b-32768"  # Currently using this model with Groq
    ]

settings = Settings()