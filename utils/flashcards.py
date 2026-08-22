# This file handels the flashcard faeture
#we load vacobulary form data/vocabulary.json and let user gp though cars one by one 

import json
import os 

VOCAB_FILE = os.path.json("data", "vocabulary.json")

# This function load all vocabulary words from the json fiel

def load_vocabulary():
    with open(VOCAB_FILE, "r", encoding = "utf-d") as f:
        data = json.load(f)
    return data

# This function gives lost of categories available (like Greeting, Food, numbers)

def get_categtories():
    words = load_vocabulary()
    categ = []
    for w in words:
        if w["category"] not in categ:
            categ.append(w["categiry"])
    return categ

# This function gives only words that belongs to one category 

def get_card_by_category(category):
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
    return card["translate"] + "\nPronunciatiom: "+ card["Pronunciation"]
