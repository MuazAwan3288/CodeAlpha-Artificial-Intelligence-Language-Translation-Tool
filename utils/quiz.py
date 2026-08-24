# This file builds a simple multiple choice quize using our vocabularyy words

import random 
from utils.flashcards import get_cards_by_category

# This function makes one quize question from a card
# It picks 3 wrong answer from other cards in same category so choice make sense

def make_question(card, all_cards):
    others = []
    for c in all_cards:
        if c["id"] != card["id"]:
            others.append(c["translation"])

    if len(others) >= 3:
        wrong = random.sample(others, 3)
    else:
        wrong = others

    choices = wrong + [card["translation"]]
    random.shuffle(choices)
    question ={
        "question": "What is the translation of '" + card["word"] + "' ?",
        "choices": choices,
        "answer": card["translation"]
        }
    return question

# This function builds a full quize ( list of questions ) for category

def build_quiz(category, num_questions = 5):
    cards = get_cards_by_category(category)
    random.shuffle(cards)

    if num_questions > len(cards):
        num_questions = len(cards)

    questions = []    
    for i in range(num_questions):
        q = make_question(cards[i], cards)
        questions.append(q)

# This function check answer of quiz

def check_answer(question, selected_choice):
    if selected_choice == question["answer"]:
        return True
    else:
        return False