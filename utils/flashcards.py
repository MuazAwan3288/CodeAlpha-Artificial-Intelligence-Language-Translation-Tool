# This file handels the flashcard faeture
#we load vacobulary form data/vocabulary.json and let user gp though cars one by one 

import json
import os 

VOCAB_FILE = os.path.join("data", "vocabulary.json")

# ===============
# LOAD VOCABULARY
# ===============

def load_vocabulary():

# Load all vocabulary words from the JSON files.

    with open(VOCAB_FILE, "r", encoding = "utf-8") as f:
        data = json.load(f)
    return data

# ==============
# GET CATEGORIES
# ==============

def get_categories():

# Return a list of available vocabulary categories.

    words = load_vocabulary()
    categories = []
    for w in words:
        if w["category"] not in categories:
            categories.append(w["category"])
    return categories

# ======================
# GET CARDS BBY CATEGORY
# ======================

def get_cards_by_category(category, language):

# Return only cards belonging to the selected category.

    words = load_vocabulary()
    cards = []
    for w in words:
        if w["category"] == category:
            cards.append(w)
    return cards

# This function shows front sode of card (the question word, not the answer)

def get_card_front(card):
    return card["word"] + " ("+ card["language"]+")"

# This function shows back side of card (answer + how to say it)

def get_card_back(card):
    return card["translation"] + "\nPronunciatiom: "+ card["pronunciation"]
