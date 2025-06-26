import sys
from src.transcription.youtube import YouTubeTranscriber
from src.transcription.local import LocalFileTranscriber
from src.minutes.generator import MeetingMinutesGenerator

def main():
    print("Meeting Minutes Generator\n")
    use_youtube = input("Transcribe from YouTube? (y/n): ").strip().lower() == 'y'
    if use_youtube:
        youtube_url = input("Enter YouTube video URL: ").strip()
        transcriber = YouTubeTranscriber(youtube_url)
    else:
        file_path = input("Enter local file path: ").strip()
        transcriber = LocalFileTranscriber(file_path)

    print("\nTranscribing... This may take a while.")
    transcript = transcriber.transcribe()
    print("\nTranscript preview:\n")
    print(transcript[:1000])

    print("\nGenerating meeting minutes...")
    generator = MeetingMinutesGenerator()
    minutes = generator.generate_minutes(transcript)
    print("\n=== Meeting Minutes ===\n")
    print(minutes)

if __name__ == "__main__":
    main()
