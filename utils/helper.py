# This file has some small functions that we need in the app
# It manages supported languages and Huggingface models name.

# ===================
# SUPPORTED LANGUAGES
# ===================

language_list = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Urdu": "ur"
    }

# =================
# GET LANGUAGE LIST
# =================

def get_language():

# Return name of all supported languages.

    return list(language_list.keys())

# ================
# CHECK USER INPUT
# ================

def check_input(text, from_lang, to_lang):

# This function checks user input is ok or not.

    if text is None or text.strip() == "":
        return False, "Please Write Some Thing to Translate"

    if text.isspace() == True:
        return False, "Please Write Some Thing to Translate"

    if from_lang not in language_list:
        return False, "Source Language is not Available"

    if to_lang not in language_list:
        return False, "Target Language is not Available"

    if from_lang == to_lang:
        return False, "Please Select Different Language"

# IF aLL Okay

    return True, "OK"

# ===========================
# GET HUGGING FACE MODEL NAME
# ===========================

def get_model(from_lang, to_lang):
    
# This function generate the huggingface translation model name
# Example: English -> French
# Helsinki-NLP/opus-mt-en-fr

    code1 = language_list[from_lang]
    code2 = language_list[to_lang]

    model_name = f"Helsinki-NLP/opus-mt-{code1}-{code2}"
    return model_name