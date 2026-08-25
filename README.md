# 🌍 AI Language Translation & Learning Tool

An AI-powered language translation and learning application built with Python, Gradio, Hugging Face Transformers, PyTorch, and gTTS.

The application provides text translation as well as additional learning features such as flashcards, quizzes, pronunciation audio, and progress tracking.

---

## ✨ Features

### 🌍 AI Translator

- Translate text between supported languages
- Uses Hugging Face MarianMT translation models
- Supports multiple languages
- Automatically loads translation models when required
- Reuses loaded models to improve performance
- Supports CPU and GPU when available
- Input validation and error handling

### 🃏 Flashcards

- Learn vocabulary using flashcards
- Select vocabulary categories
- View the word and language
- Reveal the translation and pronunciation
- Move to the next or previous card
- Track flashcards viewed

### 📝 Quiz

- Multiple-choice vocabulary quizzes
- Questions are generated from vocabulary data
- Randomized answer choices
- Instant answer feedback
- Automatic score calculation
- Quiz scores are saved for progress tracking

### 🔊 Pronunciation

- Generate pronunciation audio using gTTS
- Audio files are saved in the assets/audio folder
- Supports language-specific pronunciation

### 📊 Progress Tracking

- Track flashcards viewed
- Track quizzes completed
- Store quiz scores
- View the latest quiz result
- Progress is stored locally in JSON format

---

## 🛠️ Technologies Used

- **Python**
- **Gradio**
- **PyTorch**
- **Hugging Face Transformers**
- **MarianMT / Helsinki-NLP translation models**
- **gTTS**
- **JSON**

---

## 📁 Project Structure

```text
CodeAlpha-Artificial-Intelligence-Language-Translation-Tool/
│
├── .gradio/
├── .vscode/
│
├── assets/
│   ├── audio/
│   ├── icons/
│   └── images/
│
├── config/
│   ├── languages.json
│   └── models.json
│
├── data/
│   ├── lessons.json
│   ├── progress.json
│   └── vocabulary.json
│
├── utils/
│   ├── flashcards.py
│   ├── helper.py
│   ├── progress.py
│   ├── quiz.py
│   └── tts.py
│
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
└── translator.py