from google import genai
from google.genai import types
from src.config import get_gemini_api_key

class GeminiClient:
    """Wrapper for the Gemini API client."""
    def __init__(self):
        api_key = get_gemini_api_key()
        self.client = genai.Client(api_key=api_key)

    def generate_content(self, *args, **kwargs):
        return self.client.models.generate_content(*args, **kwargs)

    def upload_file(self, file_path: str):
        return self.client.files.upload(file=file_path) 