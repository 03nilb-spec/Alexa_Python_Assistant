
# Alexa Python Voice Assistant

This is a simple Python-based voice assistant inspired by Amazon Alexa. It can recognize your voice, respond using speech, and perform basic tasks like:

- Playing songs on YouTube  
- Telling the current date and time  
- Telling jokes  
- Answering questions using Wikipedia  

---

## Features

- Voice-activated commands using your microphone
- Text-to-speech responses with a female voice
- Integration with:
  - **YouTube** (via `pywhatkit`) for music
  - **Wikipedia** for quick facts
  - **pyjokes** for light-hearted humor

---

## Setup Instructions

### 1. Clone the repository

``` bash
git clone https://github.com/yourusername/alexa-python-assistant.git
cd alexa-python-assistant
```

### 2 Install the dependencies
``` bash
pip install -r requirements.txt
```

### 3 How to Run
Just run the Python file:
``` bash
alexa.py
```

## Notes
Make sure your microphone is working properly.

PyAudio is required for microphone access. 
