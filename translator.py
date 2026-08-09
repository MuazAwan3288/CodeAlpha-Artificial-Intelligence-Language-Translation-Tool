"""
translator.py
--------------
Core translation engine using Hugging Face's M2M100 multilingual model.
"""

from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

MODEL_NAME = "facebook/m2m100_418M"


class Translator:
    def __init__(self, model_name: str = MODEL_NAME):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self._load_model()

    def _load_model(self):
        print(f"[translator] Loading model '{self.model_name}'...")
        self.tokenizer = M2M100Tokenizer.from_pretrained(self.model_name)
        self.model = M2M100ForConditionalGeneration.from_pretrained(self.model_name)
        print("[translator] Model loaded successfully.")

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        if not text or not text.strip():
            return ""

        self.tokenizer.src_lang = source_lang
        encoded = self.tokenizer(text, return_tensors="pt")

        generated_tokens = self.model.generate(
            **encoded,
            forced_bos_token_id=self.tokenizer.get_lang_id(target_lang),
            max_length=512,
        )

        translated = self.tokenizer.batch_decode(
            generated_tokens, skip_special_tokens=True
        )
        return translated[0]


_translator_instance = None


def get_translator() -> Translator:
    global _translator_instance
    if _translator_instance is None:
        _translator_instance = Translator()
    return _translator_instance


def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    translator = get_translator()
    return translator.translate(text, source_lang, target_lang) 