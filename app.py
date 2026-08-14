#app.py
#main file with gradio ui

from pickle import APPEND

import gradio as gr
import translator
from utils import helper

#This object will load and resuse translation model

translator_model = translator.Translator()

#function when translator button clicked

def do_translate(text, lang1, lang2):
    ok, msg = helper.check_input(text,lang1,lang2)

    if ok == False:
        return msg
    ans = translator_model.do_translation(text, lang1, lang2)

    return ans    

#function when clear button clicked
def do_clear():
    return "", "English",""

#make app

def main():
    language = helper.get_language()
    with gr.Blocks() as app:
        gr.Markdown("##Language Translator ")

        with gr.Row():
            lang1 = gr.Dropdown(language, label= "From", value= "English")
            lang2 = gr.Dropdown(language, label= "To", value= "French")

        with gr.Row():
            txt_in = gr.Textbox(label= "Input", lines= 4)
            txt_out = gr.Textbox(label= "Output", lines= 4)

        with gr.Row():
            btn1 = gr.Button("Translate")
            btn2 = gr.Button("Clear")

            btn1.click(do_translate, inputs=[txt_in, lang1, lang2], outputs= txt_out)
            btn2.click(do_clear, outputs= [txt_in, lang1, txt_out])

    app.launch(share=True)
if __name__ == "__main__":
    main()
    