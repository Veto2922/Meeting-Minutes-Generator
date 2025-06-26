from abc import ABC, abstractmethod

class BaseTranscriber(ABC):
    @abstractmethod
    def transcribe(self) -> str:
        """Transcribe the audio/video and return the transcript as text."""
        pass 