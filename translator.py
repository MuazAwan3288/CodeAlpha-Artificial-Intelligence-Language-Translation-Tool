#This file loads the model and does translation

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from utils.helper import get_model
class Translator:
    def __init__(self):
#we keep models in memory so we dont download again
#we use dictionary to store models with their name as key
        self.models = {}
        self.tokenizers = {}

        if torch.cpu.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"

# print("Using device:" self.device) # for checking CPU/GPU
# this loads model if not already loaded

    def load_model(self, model_name):
        if model_name not in self.models:
            tok = AutoTokenizer.from_pretrained(model_name)
            mod = AutoModelForSeq2SeqLM.from_pretrained(model_name)

            mod = mod.to(self.device)

            self.tokenizers[model_name] = tok
            self.models[model_name] =mod

        return self.tokenizers[model_name], self.models[model_name]

#main fuction tp translate text

    def do_translation(self, text, from_lang, to_lang):
        model_name = get_model(from_lang, to_lang)

        try:
            tokenizer, model = self.load_model(model_name)
 #covert text to tokens
            inputs = tokenizer(text, return_tensors = "pt", padding = True, truncation = True)
            inputs = inputs.to(self.device)
#generate translation
            with torch.no_grad():
                outputs = model.generate(**inputs, max_length = 512)
#convert token back to text
            result = tokenizer.decode(outputs[0], skip_special_tokens= True)
            return result
        except Exception as e:
            return "Sorry translation failed. Please try again later"
