# ====================================
# TEST TO SPEECH (TTS)                  
# ====================================
#                                                       
# This file creates ausio prounciation
# Using Google Text-to-Speech (gTTS)    
#                                                       
# =====================================

import os
import hashlib
from gtts import gTTS

# ============
# AUDIO FOLDER
# ============

AUDIO_FOLDER = os.path.join("assets", "audio")

# ===================
# CREATE AUDIO FOLDER
# ===================

def create_audio_folder():
    if not os.path.exists(AUDIO_FOLDER):
        os.makedirs(AUDIO_FOLDER, exist_ok = True)

# ==========
# MAKE AUDIO
# ==========

def make_audio(text, lang_code):

    create_audio_folder()
    text = text.strip()

    if not text:
        return None

    try:

        file_hash = hashlib.md5(f"{text}_{lang_code}".encode("utf-8")).hexdigest()
        file_path = os.path.join(AUDIO_FOLDER, f"{file_hash}.mp3")

        if os.path.exists(file_path):
            return file_path
    
        speech = gTTS(text = text, lang = lang_code, slow = False)
        speech.save(file_path)

        if os.path.exists(file_path):
            return file_path

        return None

    except Exception as e:
        print("TTS error: ", e)
        return None
