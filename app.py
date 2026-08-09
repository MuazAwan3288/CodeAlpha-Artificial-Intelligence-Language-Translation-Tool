"""
app.py
------
Gradio web interface for the AI Language Translation Tool.
"""

import gradio as gr

from translator import translate_text
from utils.helper import get_language_names, get_language_code, is_valid_input


def translate_interface(text: str, source_language: str, target_language: str) -> str:
    if not is_valid_input(text):
        return "⚠️ Please enter some text to translate."

    source_code = get_language_code(source_language)
    target_code = get_language_code(target_language)

    if source_code == target_code:
        return "⚠️ Source and target languages must be different."

    try:
        return translate_text(text, source_code, target_code)
    except Exception as e:
        return f"❌ Translation failed: {e}"


def build_app() -> gr.Blocks:
    languages = get_language_names()

    with gr.Blocks(title="AI Language Translator") as demo:
        gr.Markdown("# 🌍 AI Language Translation Tool")
        gr.Markdown(
            "Translate text between multiple languages using a Hugging Face "
            "multilingual translation model (M2M100). Built for the "
            "CodeAlpha internship."
        )

        with gr.Row():
            with gr.Column():
                source_lang = gr.Dropdown(
                    choices=languages, value="English", label="Source Language"
                )
                input_text = gr.Textbox(
                    lines=6, label="Enter text to translate", placeholder="Type here..."
                )
            with gr.Column():
                target_lang = gr.Dropdown(
                    choices=languages, value="Urdu", label="Target Language"
                )
                output_text = gr.Textbox(
                    lines=6, label="Translated text", interactive=False
                )

        translate_btn = gr.Button("Translate", variant="primary")
        clear_btn = gr.Button("Clear")

        translate_btn.click(
            fn=translate_interface,
            inputs=[input_text, source_lang, target_lang],
            outputs=output_text,
        )
        clear_btn.click(
            fn=lambda: ("", ""),
            inputs=None,
            outputs=[input_text, output_text],
        )

        gr.Examples(
            examples=[
                ["Hello, how are you?", "English", "French"],
                ["I love programming.", "English", "Urdu"],
                ["Wie geht es dir?", "German", "English"],
            ],
            inputs=[input_text, source_lang, target_lang],
        )

    return demo


if __name__ == "__main__":
    app = build_app()
    app.launch()