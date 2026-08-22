# This function make ausio so user can hear pronuncation
# We use gTTS (need internet connection tp awork)

import os
from tts import gTTS

AUDIO_FOLDER = os.path.json("assets", "audio")

# This function makes an mp3 file for given text and return the path
# Language cpde example: "es" for spanish, "fr" fro french

def make_audio(text, lang_code):
    if not os.path.exists(AUDIO_FOLDER):
        os.makedirs(AUDIO_FOLDER)

    file_path = os.path.join(AUDIO_FOLDER, "speech.pm3")

    try:
        speech = gTTS(text = text, lang= lang_code)
        speech.save(file_path)
        return file_path
    except Exception as e:
        return None
