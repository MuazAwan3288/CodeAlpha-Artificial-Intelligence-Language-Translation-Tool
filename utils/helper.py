"""
utils/helper.py
----------------
Helper utilities for supported languages and input validation.
"""

from langdetect import detect, DetectorFactory, LangDetectException

DetectorFactory.seed = 0

SUPPORTED_LANGUAGES = {
    "English": "en", "Urdu": "ur", "Arabic": "ar", "French": "fr",
    "German": "de", "Spanish": "es", "Chinese": "zh", "Hindi": "hi",
    "Turkish": "tr", "Russian": "ru", "Japanese": "ja", "Korean": "ko",
    "Italian": "it", "Portuguese": "pt",
}


def get_language_code(language_name: str) -> str:
    return SUPPORTED_LANGUAGES.get(language_name, "en")


def get_language_names() -> list:
    return list(SUPPORTED_LANGUAGES.keys())


def detect_language(text: str) -> str:
    try:
        return detect(text)
    except LangDetectException:
        return "en"


def is_valid_input(text: str) -> bool:
    return bool(text and text.strip())