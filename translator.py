# This file loads Hugging face translation models and perform translation

import torch
from transformers import (AutoTokenizer, AutoModelForSeq2SeqLM)
from utils.helper import get_model
class Translator:
    def __init__(self):

# Store loadedd models in memory.
# This prevents downloadiinig/loading them repeatedly.

        self.models = {}
        self.tokenizers = {}

        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"

# ==========
# LOAD MODEL
# ==========

    def load_model(self, model_name):

# Load only if model isn't alrready loaded.

        if model_name not in self.models:
            tok = AutoTokenizer.from_pretrained(model_name)
            mod = AutoModelForSeq2SeqLM.from_pretrained(model_name)

            mod = mod.to(self.device)

            self.tokenizers[model_name] = tok
            self.models[model_name] =mod

        return self.tokenizers[model_name], self.models[model_name]

# =========
# TRANSLATE
# =========

    def do_translation(self, text, from_lang, to_lang):

# Main fuction tp translate text

        model_name = get_model(from_lang, to_lang)

        try:
            tokenizer, model = self.load_model(model_name)
# Covert text to tokens
            inputs = tokenizer(text, return_tensors = "pt", padding = True, truncation = True)
            inputs = inputs.to(self.device)
# Generate translation
            with torch.no_grad():
                outputs = model.generate(**inputs, max_length = 512)
# Convert token back to text
            result = tokenizer.decode(outputs[0], skip_special_tokens= True)
            return result
        except Exception as e:
            return "Sorry translation failed. Please try again later"
