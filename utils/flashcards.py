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

# =====================
# GET CARDS BY CATEGORY
# =====================

def get_cards_by_category(category, language = None):

# Return only cards belonging to the selected category.

    words = load_vocabulary()
    cards = []
    for w in words:
        if w["category"] == category:
            if language is None or w["language"] == language:
                cards.append(w)
    return cards

# ==========
# CARD FRONT
# ==========

def get_card_front(card):

# This function return front side of card (the question word, not the answer)

    return card["word"] + " ("+ card["language"]+")"

# =========
# CARD BACK
# =========

def get_card_back(card):

# This function return back side of card (answer + how to say it)

    return card["translation"] + "\nPronunciation: "+ card["pronunciation"]
