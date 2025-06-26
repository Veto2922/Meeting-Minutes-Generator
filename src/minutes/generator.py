from src.client.gemini import GeminiClient
from google.genai import types

SYSTEM_PROMPT = """
You are a professional meeting assistant. You will be given a transcript of a meeting from a video or audio recording.
Your task is to generate clear and concise **Meeting Minutes** in a structured format that includes the following sections:
1. **Meeting Title** (if mentioned)
2. **Date & Time**
3. **Attendees**
4. **Agenda Items**
5. **Discussion Summary**
6. **Decisions Made**
7. **Action Items**
8. **Next Meeting**
📌 Make the minutes formal and easy to read.
📌 If some information is missing, write: [Not mentioned].
Now here is the transcript:
"""

class MeetingMinutesGenerator:
    def __init__(self, model: str = "gemini-2.0-flash"):
        self.model = model
        self.client = GeminiClient()

    def generate_minutes(self, transcript: str) -> str:
        response = self.client.generate_content(
            model=self.model,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT.strip()
            ),
            contents=transcript
        )
        return response.text 