# This file saves and loads progree
# We just use a sample json file, no database needed for this project

import json
import os

PROGRESS_FIle = os.path.join("data", "progress.json")

# =============
# LOAD PROGRESS
# =============

def load_progress():
    
# This function loads progree from file, if file missing we start fresh

    if not os.path.exists(PROGRESS_FIle):
        return {"lessons_done": [], "quiz_scores": [], "cards_seen": 0}

    with open(PROGRESS_FIle, "r", encoding = "utf-8") as f:
        data = json.load(f)
    return data

# =============
# SAVE PROGRESS
# =============

def save_progress(data):

# This function save progree back tp file.

    with open(PROGRESS_FIle, "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 4)

# ==============
# ADDD CARD VIEW
# ==============

def add_card_seen():

# Increase the number of viewed flashcards.
    
    data = load_progress()
    data["cards_seen"] = data["cards_seen"] + 1
    save_progress(data)
    return data["cards_seen"]

# ==============
# ADD QUIZ SCORE
# ==============

def add_quiz_score(score, total):

# Save a coplete quize score.

    data = load_progress()
    data["quiz_scores"].append({"score": score, "total": total})
    save_progress(data)

# ================
# PROGRESS SUMARRY
# ================

def get_summary():

# Create a rreadable progress summary.
#     
    data = load_progress()    
    total_quizzes = len(data["quiz_scores"])

    text = "Flashcard viewed: "+ str(data["cards_seen"]) + "\n"
    text = text + "Quize taken: "+ str(total_quizzes)+ "\n"

    if total_quizzes > 0:
        last = data["quiz_scores"][-1]
        text = text + "Last quize score: "+ str(last["score"])+ "/"+ str(last["total"])
    return text