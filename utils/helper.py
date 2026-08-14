#this file has some small functions that we need in the app
# we make a list of languages with their short codes 
# huggingface modelss need codes like en, fr, de etc 

language_list = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Urdu": "ur"
    }

#this function will return all languages name for dropdown menu

def get_language():
    name = []
    for i in language_list:
        name.append(i)
    return name

#this function checks if user inout is ok or not 

def check_input(text, from_lang, to_lang):

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

#This function makes the model name for huggingface
#example: Helsinki-NLP/opus-mt-en-fr

def get_model(from_lang, to_lang):
    code1 = language_list[from_lang]
    code2 = language_list[to_lang]

    model_name = f"Helsinki-NLP/opus-mt-{code1}-{code2}"
    return model_name

