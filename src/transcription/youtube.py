from src.transcription.base import BaseTranscriber
from src.client.gemini import GeminiClient
from google.genai import types

class YouTubeTranscriber(BaseTranscriber):
    def __init__(self, youtube_url: str, model: str = "gemini-2.5-flash"):
        self.youtube_url = youtube_url
        self.model = model
        self.client = GeminiClient()

    def transcribe(self) -> str:
        response = self.client.generate_content(
            model=self.model,
            contents=types.Content(
                parts=[
                    types.Part(file_data=types.FileData(file_uri=self.youtube_url)),
                    types.Part(text="Transcribe the audio from this video.")
                ]
            )
        )
        return response.text 