# AI Language Translation Tool

This is a simple AI-powered language translation tool built with Python.

The application uses pretrained Hugging Face Transformer models to translate text between different languages and Gradio to provide a simple web interface.

## Features

- Translate text between multiple languages
- Uses pretrained AI translation models from Hugging Face
- Supports CPU and GPU
- Simple and beginner-friendly Gradio interface
- Input validation
- Translate and Clear buttons
- Reuses loaded models to avoid unnecessary downloads

## Languages Supported

- English
- French
- German
- Spanish
- Italian
- Portuguese
- Urdu

## Technologies Used

- Python 3.12
- PyTorch
- Hugging Face Transformers
- SentencePiece
- Gradio

## Project Structure

```text
CodeAlpha-Artificial-Intelligence-Language-Translation-Tool/
│
├── assets/
│   └── images/
│
├── utils/
│   └── helper.py
│
├── app.py
├── translator.py
├── requirements.txt
├── README.md
└── .gitignore