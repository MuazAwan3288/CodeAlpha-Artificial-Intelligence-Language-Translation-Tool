# =============================================
# LANGUAGE TRANSLATOR AND LEARNING APP
# =============================================
#
# This application contains four main features:
#
# 1. Translator
# 2. Flashcards
# 3. Quiz
# 4. Progress Tracking
#
# =============================================

import gradio as gr

import translator

from utils import helper
from utils import flashcards
from utils import quiz
from utils import progress
from utils import tts


# ================
# TRANSLATOR MODEL
# ================

# Create one Translator object.
# Models are stored in memory and reused.

translator_model = translator.Translator()

# ====================
# TRANSLATOR FUNCTIONS
# ====================

def do_translate(text, lang1, lang2):

# Validate input.

    ok, message = helper.check_input(text,lang1,lang2)
    if not ok:
        return message

# Perform translation.

    result = translator_model.do_translation(text, lang1, lang2)
    return result


def do_clear():

# FIXED:
# Reset input and output.

    return "", "English", "French", ""

# ===================
# FLASHCARD FUNCTIONS
# ===================

def start_flashcards(category):
    cards = flashcards.get_cards_by_category(category)
    if len(cards) == 0:
        return ("No cards found", "", cards, 0)
    front = flashcards.get_card_front(cards[0])
    return (front, "", cards, 0)

def show_answer(cards, index):
    if not cards:
        return ""

    back = flashcards.get_card_back(cards[index])
    progress.add_card_seen()
    return back


def next_card(cards, index):
    if not cards:
        return ("No cards", "", cards, 0)

    index += 1

    if index >= len(cards):
        index = 0

    front = flashcards.get_card_front(cards[index])
    return (front, "", cards, index)

def prev_card(cards, index):
    if not cards:
        return ("No cards", "", cards, 0)

    index -= 1

    if index < 0:
        index = len(cards) - 1

    front = flashcards.get_card_front(cards[index])
    return (front, "", cards, index)

def play_pronunciation(cards, index):
    if not cards:
        return None

    card = cards[index]
    path = tts.make_audio(card["translation"], card["lang_code"])
    return path

# ==============
# QUIZ FUNCTIONS
# ==============

def start_quiz(category):
    questions = quiz.build_quiz(category, 5)
    if len(questions) == 0:
        return ("No questions available.", gr.update(choices=[]), questions, 0, 0)

    question = questions[0]
    return (question["question"],gr.update(choices=question["choices"], value=None), questions, 0, 0)

def submit_answer(questions, index, score, selected):
    if not questions:
        return ("Please start the quiz first.", gr.update(),questions, index, score)

    if selected is None:
        return ("Please select an answer.", gr.update(), questions, index, score)

    current_question = questions[index]
    correct = quiz.check_answer(current_question, selected)

    if correct:
        score += 1
        message = "✅ Correct!"

    else:

        message = ("❌ Wrong! Correct answer: " + current_question["answer"])
    index += 1

# Quiz finished.
    if index >= len(questions):
        progress.add_quiz_score(score, len(questions))
        final_message = (message + "\n\n" + "🎉 Quiz finished!" + "\n" + "Your Score: " + str(score) + "/" + str(len(questions)))
        return (final_message, gr.update(choices=[]), questions, index, score)

# Show next question.
    
    next_question = questions[index]
    return (message + "\n\n" + next_question["question"],gr.update(choices=next_question["choices"], value=None), questions, index, score)

# ========
# PROGRESS
# ========

def refresh_progress():
    return progress.get_summary()

# ================
# MAIN APPLICATION
# ================

def main():
    languages = helper.get_language()
    categories = flashcards.get_categories()
    with gr.Blocks(title="AI Language Translation & Learning Tool") as app:

# ======
# HEADER
# ======

        gr.Markdown(
            """
            # 🌍 AI Language Translation & Learning Tool

            Translate text, learn vocabulary with flashcards,
            test your knowledge with quizzes, and track your progress.
            """
        )

# ====
# TABS
# ====

        with gr.Tabs():

# ==========
# TRANSLATOR
# ==========

            with gr.Tab("🌍 Translator"):

                with gr.Row():

                    lang1 = gr.Dropdown(choices=languages, label="From", value="English")
                    lang2 = gr.Dropdown(choices=languages, label="To", value="French")

                with gr.Row():

                    txt_in = gr.Textbox(label="Input Text", placeholder="Enter text to translate...", lines=6)
                    txt_out = gr.Textbox(label="Translation", lines=6, interactive=False)

                with gr.Row():

                    translate_btn = gr.Button("🔄 Translate", variant="primary")
                    clear_btn = gr.Button("🗑️ Clear")

                translate_btn.click(fn=do_translate, inputs=[txt_in, lang1, lang2], outputs=txt_out)
                clear_btn.click(fn=do_clear, outputs=[txt_in,lang1, lang2, txt_out])

# ==========
# FLASHCARDS
# ==========

            with gr.Tab("🃏 Flashcards"):

                cat_dropdown = gr.Dropdown(choices=categories, label="Category", value=(categories[0] if categories else None))
                start_btn = gr.Button("▶ Start Flashcards", variant="primary")
                card_front = gr.Textbox(label="Word", interactive=False)
                card_back = gr.Textbox(label="Answer", interactive=False, lines=3)
                audio_out = gr.Audio(label="🔊 Pronunciation")
                cards_state = gr.State([])
                index_state = gr.State(0)

                with gr.Row():

                    show_btn = gr.Button("👁️ Show Answer")
                    speak_btn = gr.Button("🔊 Play Pronunciation")

                with gr.Row():

                    prev_btn = gr.Button("⬅ Previous")
                    next_btn = gr.Button("Next ➡")
                start_btn.click(start_flashcards,
                    inputs=cat_dropdown,
                    outputs=[card_front, card_back, cards_state, index_state])

                show_btn.click(show_answer, inputs=[cards_state, index_state], outputs=card_back)
                next_btn.click(next_card, inputs=[cards_state, index_state], outputs=[card_front, card_back, cards_state, index_state])
                prev_btn.click(prev_card, inputs=[cards_state, index_state], outputs=[card_front, card_back, cards_state, index_state])
                speak_btn.click(play_pronunciation, inputs=[cards_state, index_state], outputs=audio_out)


# ====
# QUIZ
# ====

            with gr.Tab("📝 Quiz"):

                quiz_cat = gr.Dropdown(choices=categories, label="Category", value=(categories[0] if categories else None))
                quiz_start_btn = gr.Button("▶ Start Quiz", variant="primary")

                question_box = gr.Textbox(label="Question", interactive=False, lines=2)
                choices_box = gr.Radio(label="Choose your answer", choices=[])

                submit_btn = gr.Button("Submit Answer")
                questions_state = gr.State([])

                q_index_state = gr.State(0)
                score_state = gr.State(0)

                quiz_start_btn.click(start_quiz, inputs=quiz_cat, outputs=[ question_box, choices_box, questions_state, q_index_state, score_state])
                submit_btn.click(submit_answer, inputs=[questions_state, q_index_state, score_state, choices_box], outputs=[ question_box, choices_box, questions_state, q_index_state, score_state])

# ========
# PROGRESS
# ========

            with gr.Tab("📊 Progress"):

                gr.Markdown(
                    """
                    ## 📊 Your Learning Progress

                    Check your flashcard and quiz activity.
                    """
                )

                progress_box = gr.Textbox(label="Progress", interactive=False, lines=5)
                refresh_btn = gr.Button("🔄 Refresh Progress")
                refresh_btn.click(refresh_progress, outputs=progress_box)


# ======
# FOOTER
# ======

        gr.Markdown(
            """
            ---
            **AI Language Translation & Learning Tool**

            Built with Python, Gradio, Hugging Face Transformers,
            PyTorch and gTTS.
            """
        )

# =========
# START APP
# =========

    app.launch(share=True)

# ===
# RUN
# ===

if __name__ == "__main__":
    main()