# This function create audio so user can hear pronuncation
# gTTS requiresa an internet connection

import os
import hashlib
from gtts import gTTS

AUDIO_FOLDER = os.path.join("assets", "audio")

# ============
# CREATE AUDIO
# ============

def make_audio(text, lang_code):

# Generate an mp3 pronunciation file.
# This filename is based on the texr and language sa different prounciation do not overwrite each other.

    if not os.path.exists(AUDIO_FOLDER):
        os.makedirs(AUDIO_FOLDER)

    unique_id = hashlib.md5(f"{text}_{lang_code}".encode("utf-8")).hexdigest()
    file_path = os.path.join(AUDIO_FOLDER, f"{unique_id}.mp3")

    if os.path.exists(file_path):
        return file_path
    try:
        speech = gTTS(text = text, lang = lang_code)
        speech.save(file_path)
        return file_path

    except Exception as e:
        print("TTS error: ", e)
        return None