# 🔥 Aagni AI Desktop Assistant

Aagni is a Python-powered AI desktop assistant that interacts with users via natural voice commands. Leveraging OpenAI's GPT model, it can answer queries, perform system tasks, and provide real-time information with a sleek GUI interface.

---

## 🚀 Features

- 🎙️ **Voice Interaction**: Understands spoken commands using SpeechRecognition.
- 🧠 **AI-Powered Conversations**: Uses OpenAI's GPT model for intelligent, human-like responses.
- 🖥️ **System Task Automation**: Opens apps, searches Google, tells the time, weather updates, jokes, and more.
- 🗣️ **Text-to-Speech Output**: Replies with voice using pyttsx3 or gTTS.
- 🖼️ **GUI Interface**: User-friendly desktop application built with PyQt5.
- 🔌 **Modular Design**: Easily extend functionality by adding new commands or modules.

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **AI Integration**: OpenAI GPT API
- **Voice Input**: SpeechRecognition, PyAudio
- **Voice Output**: pyttsx3 / gTTS
- **GUI**: PyQt5
- **APIs Used**: OpenWeatherMap, Webbrowser, etc.

---

## 📸 Demo

> _(Insert a screen recording or screenshot of the assistant here)_

---

## 🧩 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/aagni-ai-assistant.git
   cd aagni-ai-assistant
2. pip install -r requirements.txt
3. Create a .env file and add: OPENAI_API_KEY=your_openai_api_key_here
4. Run the app : python main.py

## 📂 Project Structure
aagni-ai-assistant/
│
├── main.py                # Entry point for the assistant
├── assistant/             # Core logic: input, output, GPT communication
│   ├── voice_input.py
│   ├── tts_output.py
│   ├── gpt_engine.py
│   └── commands.py
├── ui/                    # PyQt5 GUI files
│   └── main_window.ui
├── .env                   # API keys (not pushed to Git)
├── requirements.txt       # Python dependencies
└── README.md
