# This file create a simple multiple choice quiz
# using vocabulary words

import random 
from utils.flashcards import get_cards_by_category

# =================
# MAKE ONE QUESTION
# =================

def make_question(card, all_cards):

# Create one multiple choice question
# The correct answer comes from the selected card.Three wrong answers are selected from other cards.

    others = []
    for other_cards in all_cards:
        if other_cards["id"] != card["id"]:
            others.append(other_cards["translation"])

    
    wrong_answers = random.sample(others, min(3, len(others)))
    choices = wrong_answers + [card["translation"]]
    random.shuffle(choices)
    question ={
        "question": "What is the translation of '" + card["word"] + "' ?",
        "choices": choices,
        "answer": card["translation"]
        }
    return question

# ==========
# BUILD QUIZ
# ==========

def build_quiz(category, num_questions = 5):

# Build a complet quiz for the selected category
     
    cards = get_cards_by_category(category)
    if not cards:
        return []
    
    random.shuffle(cards)

    if num_questions > len(cards):
        num_questions = len(cards)

    questions = []    
    for i in range(num_questions):
        q = make_question(cards[i], cards)
        questions.append(q)

    return questions

# ============
# CHECK ANSWER
# ============

def check_answer(question, selected_choice):

# Check whether the selected answer is correct.

    return selected_choice == question["answer"]
    