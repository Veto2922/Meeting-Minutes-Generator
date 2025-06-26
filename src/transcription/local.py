from src.transcription.base import BaseTranscriber
from src.client.gemini import GeminiClient
from google.genai import types

class LocalFileTranscriber(BaseTranscriber):
    def __init__(self, file_path: str, model: str = "gemini-2.5-flash"):
        self.file_path = file_path
        self.model = model
        self.client = GeminiClient()

    def transcribe(self) -> str:
        uploaded_file = self.client.upload_file(self.file_path)
        response = self.client.generate_content(
            model=self.model,
            contents=["Generate a transcript of the speech.", uploaded_file]
        )
        return response.text 