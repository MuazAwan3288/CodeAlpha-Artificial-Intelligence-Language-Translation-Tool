# app.py
# Main file with gradio ui
# Now this app has 4 tabs: Translator, Flashcasrds, Quiz, Progress

import gradio as gr
import translator
from utils import helper
from utils import flashcards
from utils import quiz
from utils import progress
from utils import tts

# This object will load and resuse translation model
translator_model = translator.Translator()

#==================TRANSLATOR TAB =================
# Function when translator button clicked

def do_translate(text, lang1, lang2):
    ok, msg = helper.check_input(text,lang1,lang2)

    if ok == False:
        return msg
    ans = translator_model.do_translation(text, lang1, lang2)

    return ans    

# Function when clear button clicked

def do_clear():
    return "", "English",""

#==================FLASHCARDS TAB =================

def start_flashcards(category):
    cards = flashcards.get_cards_by_category(category)

    if len(cards) == 0:
        return "No cards found", "", cards, 0

    front = flashcards.get_card_front(cards[0])
    return front,"", cards, 0

def show_answer(cards, index):

    if len(cards) == 0:
        return ""

    back = flashcards.get_card_back(cards[index])
    progress.add_card_seen()
    return back

def next_card(cards, index):

    if len(cards) == 0:
        return "No cards", "", cards, 0
    index = index + 1

    if index >= len(cards):
        index = 0
    front = flashcards.get_card_front(cards[index])    

    return front, "", cards, index

def prev_card(cards, index):

    if len(cards) == 0:
        return "no cards", "", cards, 0
    
    index = index - 1

    if index < 0:
        index = len(cards) - 1

    front = flashcards.get_card_front(cards[index])    
    return front, "", cards, index

def play_pronunciation(cards, index):

    if len(cards) == 0:
        return None

    card = cards[index]
    path = tts.make_audio(card["translation"], card["lang_code"])
    return path

# ================== QUIZ TAB ==================
 
def start_quiz(category):
    questions = quiz.build_quiz(category, 5)
    if len(questions) == 0:
        return "No question available", gr.update(choices=[]), questions, 0, 0
    q = questions[0]
    return q["question"], gr.update(choices = q["choices"], value = None), questions, 0, 0
 
def submit_answer(questions, index, score, selected):
    if selected is None:
        return "Please select an answer", gr.update(), questions, index, score

    correct = quiz.check_answer(questions[index], selected)
    if correct:
        score = score + 1
        msg = "Correct!"
    else:
        msg = "Wrong! Correct answer was:" + questions[index]["answer"]

    index = index + 1
    if index >= len(questions):
        progress.add_quiz_score(score, len(questions))
        final = msg+ "\n\nQuiz finished! Your Score: " + str(score) + "/" + str(len(questions))
        return final, gr.update(choices=[]), questions, index, score

    next_q = questions[index]
    return msg, gr.update(choices = next_q["choices"], value = None), questions, index, score

# =============== PROGRESS TAB ===================

def refresh_progress():
    return progress.get_summary()

# =================  MAIN APP ====================

def main():
    language = helper.get_language()
    categories = flashcards.get_categories()

    with gr.Blocks() as app:
        gr.Markdown("# Language Translator and Learning App ")

        with gr.Tabs():

            with gr.Tab("Translator"):
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

            with gr.Tab("Flashcards"):
                cat_dropdown = gr.Dropdown(categories, label = "Category", value = categories[0] if categories else None)
                start_btn = gr.Button("Start")

                card_front = gr.Textbox(label = "Word", interactive = False )
                card_back = gr.Textbox(label = "Answer", interactive = False )
                audio_out = gr.Audio(label = "Prounciation" )

                cards_state = gr.State([])
                index_state = gr.State(0)

                with gr.Row():
                    show_btn = gr.Button("Show Answer")
                    speak_btn = gr.Button("Play Pronunciation")

                with gr.Row():
                    prev_btn = gr.Button("Previous")    
                    next_btn = gr.Button("Next")

                start_btn.click(start_flashcards, inputs = cat_dropdown, outputs=[card_front, card_back, cards_state, index_state])
                show_btn.click(show_answer, inputs = [cards_state, index_state], outputs = card_back)
                next_btn.click(next_card, inputs = [cards_state, index_state], outputs = [card_front, card_back, cards_state, index_state])
                prev_btn.click(prev_card, inputs = [cards_state, index_state], outputs = [card_front, card_back, cards_state, index_state])
                speak_btn.click(play_pronunciation, inputs = [cards_state, index_state], outputs = audio_out)

            with gr.Tab("Quiz"):
                quiz_cat = gr.Dropdown(categories, label = "Category", value = categories[0] if categories else None)
                quiz_start_btn = gr.Button("Start Quiz")

                question_box = gr.Textbox(label = "Question", interactive = False)
                choices_box = gr.Radio(label = "Choose your answer", choices = [])
                submit_btn = gr.Button("Submit")

                questions_state = gr.State([])
                q_index_state = gr.State(0)
                score_state = gr.State(0)

                quiz_start_btn.click(start_quiz, inputs=quiz_cat, outputs=[question_box, choices_box, questions_state, q_index_state, score_state])
                submit_btn.click(submit_answer, inputs=[questions_state, q_index_state, score_state, choices_box], outputs=[question_box, choices_box, questions_state, q_index_state, score_state])

            with gr.Tab("Progress"):
                progress_box = gr.Textbox(label="Your Progress", interactive=False, lines=5)
                refresh_btn = gr.Button("Refresh")
                refresh_btn.click(refresh_progress, outputs = progress_box)

    app.launch(share = True)

if __name__ == "__main__":
    main()