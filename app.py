import streamlit as st
from src.transcription.youtube import YouTubeTranscriber
from src.transcription.local import LocalFileTranscriber
from src.minutes.generator import MeetingMinutesGenerator
import tempfile
import os

def main():
    st.set_page_config(page_title="Meeting Minutes Generator", page_icon="📝", layout="centered")
    st.title("📝 Meeting Minutes Generator")
    st.write("Generate professional meeting minutes from YouTube videos or local audio/video files")

    option = st.radio("Choose input type:", ("YouTube Video", "Local File"))

    transcript = None
    minutes = None
    error = None

    if option == "YouTube Video":
        youtube_url = st.text_input("Enter YouTube video URL:")
        button_label = "Generate meeting minutes from YouTube"
        if st.button(button_label) and youtube_url:
            with st.spinner("Transcribing from YouTube. This may take a while..."):
                try:
                    transcriber = YouTubeTranscriber(youtube_url)
                    transcript = transcriber.transcribe()
                except Exception as e:
                    error = str(e)
            if transcript:
                st.subheader("Transcript Preview")
                st.text_area("Transcript", transcript, height=300)
                with st.spinner("Generating meeting minutes..."):
                    try:
                        generator = MeetingMinutesGenerator()
                        minutes = generator.generate_minutes(transcript)
                    except Exception as e:
                        error = str(e)
                if minutes:
                    st.subheader("Meeting Minutes")
                    st.markdown(minutes)
    else:
        uploaded_file = st.file_uploader("Upload audio or video file:", type=["mp3", "wav", "mp4", "m4a"])
        button_label = "Generate meeting minutes from file"
        if uploaded_file is not None and st.button(button_label):
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name
            with st.spinner("Transcribing local file. This may take a while..."):
                try:
                    transcriber = LocalFileTranscriber(tmp_path)
                    transcript = transcriber.transcribe()
                except Exception as e:
                    error = str(e)
            if transcript:
                st.subheader("Transcript Preview")
                st.text_area("Transcript", transcript[:2000], height=300)
                with st.spinner("Generating meeting minutes..."):
                    try:
                        generator = MeetingMinutesGenerator()
                        minutes = generator.generate_minutes(transcript)
                    except Exception as e:
                        error = str(e)
                if minutes:
                    st.subheader("Meeting Minutes")
                    st.markdown(minutes)
            os.remove(tmp_path)
    if error:
        st.error(f"Error: {error}")

if __name__ == "__main__":
    main()
