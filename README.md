# 🤖 AI Agent: Video → Audio → Transcript → Summary using OpenAI

This project is a **Multimodal AI Agent** that can automatically extract **frames and audio from a video**, transcribe the audio into text, and generate a **summary** using **OpenAI GPT models** or **Google Gemini models**.

---

## 🔍 Features

* 🎥 Extract frames & audio from video
* 🔊 Transcribe speech to text using Whisper or Google STT
* 🧠 Generate smart summaries using GPT-4o  
* 🖼️ Analyze image frames (vision-language models)
* ⚖️ Switch between OpenAI and Gemini APIs easily
* 📚 Educational and developer-friendly codebase

---

## 🔧 Tech Stack

| Category          | Tools / Libraries                         |
| ----------------- | ----------------------------------------- |
| Programming       | Python                                    |
| Generative Models | OpenAI GPT-4o, Google Gemini Pro/Flash    |
| Audio Processing  | `moviepy`, `speechrecognition`, `whisper` |
| Image Processing  | `opencv-python`, `PIL`, `base64`          |
| LLM APIs          | `openai`, `google.generativeai`           |
| Optional UI       | `Chainlit`, `Gradio`, `Streamlit`         |

---

## 🚀 How It Works

1. **Upload/Specify a video file**
2. `process_video()` extracts audio and frames
3. `transcribe_audio()` converts audio to text
4. `summarize_transcription()` uses LLM to summarize the transcript
5. Optional: `analyze_frames()` sends images to GPT/Gemini for frame-wise analysis

---

## 👁️ Use Cases

* 🎓 Lecture summarization tools
* 📅 Meeting/podcast note generators
* 🌐 Multimodal chatbot agents
* 📰 Video content summarizers

---

## 📁 Folder Structure

```
AI_Agent/
│
├── main.py                # Core pipeline logic
├── app.py                 # Chainlit/Streamlit app (optional)
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
└── assets/                # Sample media files
```

---

## 🚧 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/your-username/ai-agent.git
cd ai-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API keys

* For **OpenAI**: Add your key as `OPENAI_API_KEY` in environment or script
* For **Gemini**: Configure using `genai.configure(api_key=...)`

---

## 🌐 Example Output

```bash
✅ Extracted 12 frames
✅ Audio saved at: ./your_video.mp3
🔍 Transcript:
"This is the transcription text..."

📈 Summary:
"This video discusses how the speaker overcame their fear of public speaking..."
```

---

## 💼 License

MIT License

---

## ✨ Contributing

PRs and improvements welcome! Feel free to fork and modify.

---

## 🎓 Credits

Built with ❤️ using Python, OpenAI, and Gemini APIs.
