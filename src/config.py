import os
from dotenv import load_dotenv

def get_gemini_api_key() -> str:
    """Load and return the Gemini API key from environment variables."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment.")
    return api_key 