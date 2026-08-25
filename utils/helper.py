# This file has some small functions that we need in the app
# We make a list of languages with their short codes 
# Huggingface modelss need codes like en, fr, de etc 

language_list = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Urdu": "ur"
    }

# ============
# GET LANGUAGE
# ============

def get_language():

# This function will return all languages name 

    name = []
    for i in language_list:
        name.append(i)
    return name

# ===========
# CHECK INPUT
# ===========

def check_input(text, from_lang, to_lang):

# This function checks if user input is ok or not 

    if text is None or text == "":
        return False, "Please Write Some Thing to Translate"

    if text.isspace() == True:
        return False, "Please Write Some Thing to Translate"

    if from_lang not in language_list:
        return False, "Source Language is not Available"

    if to_lang not in language_list:
        return False, "Target Language is not Available"

    if from_lang == to_lang:
        return False, "Please Select Different Language"
    #IF ALL Okay
    return True, "OK"

# ==============
# GET MODEL NAME
# ==============

def get_model(from_lang, to_lang):
    
# This function makes the model name for huggingface
# Example: English -> French
# Helsinki-NLP/opus-mt-en-fr

    code1 = language_list[from_lang]
    code2 = language_list[to_lang]

    model_name = f"Helsinki-NLP/opus-mt-{code1}-{code2}"
    return model_name
