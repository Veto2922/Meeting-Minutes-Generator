# 📝 Meeting Minutes Generator

Generate professional meeting minutes from YouTube videos or local audio/video files.

![image](https://github.com/user-attachments/assets/df0e75b2-e57d-4e9d-ad8d-67b5fd54d984)



## Features
- 🎥 Transcribe audio from YouTube videos or uploaded files (mp3, wav, mp4, m4a)
- 📝 Automatically generate structured, formal meeting minutes
- 💡 Modern, user-friendly Streamlit web interface
- 🖥️ Command-line interface (CLI) for advanced users
- 🔒 Secure API key management via `.env` file
- 🧩 Clean, modular, OOP and SOLID-compliant codebase

## Project Structure
```
Meeting-Minutes-Generator/
├── app.py                  # Streamlit web app
├── main.py                 # CLI entry point
├── src/
│   ├── config.py           # Environment/config loading
│   ├── client/
│   │   └── gemini.py       # Gemini API client wrapper
│   ├── transcription/
│   │   ├── base.py         # Abstract base class
│   │   ├── youtube.py      # YouTube transcription
│   │   └── local.py        # Local file transcription
│   └── minutes/
│       └── generator.py    # Meeting minutes generator
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .env                    # (Not committed) Gemini API key
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Meeting-Minutes-Generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Gemini API key:**
   - Create a `.env` file in the project root:
     ```env
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

## Usage

### 1. Streamlit Web App (Recommended)

Run the following command:
```bash
streamlit run app.py
```
- Open the provided local URL in your browser.
- Choose input type (YouTube or File), provide the URL or upload a file, and click the button to generate meeting minutes.

### 2. Command-Line Interface (CLI)

Run the CLI version:
```bash
python main.py
```
- Follow the prompts to select input type and provide the required information.

## Output
- **Transcript Preview:** See the first part of the transcript before minutes are generated.
- **Meeting Minutes:** Receive a structured, formal summary of the meeting, ready to share or archive.

## Extensibility & Best Practices
- The codebase is organized using OOP and SOLID principles for easy maintenance and extension.
- Add new transcription sources or output formats by extending the relevant classes in `src/`.

## Requirements
- Python 3.8+
- `google-generativeai`
- `python-dotenv`
- `streamlit`

## License
MIT License
