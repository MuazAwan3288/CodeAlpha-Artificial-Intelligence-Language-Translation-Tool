# This file saves and loads progree so we remember how much they studied 
# We just use a sample json file, no darabase needed for this project

import json
import os

PROGRESS_FIle = os.path.join("data", "progress.json")

# This function loads progree from file, if file missing we start fresh

def load_progress():
    if not os.path.exists(PROGRESS_FIle):
        return {"lessons_done": [], "quiz_scores": [], "cards_seen": 0}

    with open(PROGRESS_FIle, "r", encoding = "utf-8") as f:
        data = json.load(f)
    return data

# This function save progree back tp file

def save_progress(data):
    with open(PROGRESS_FIle, "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 4)

# Call this function everytime user views a flashcard answer

def add_card_seen():
    data = load_progress()
    data["cards_seen"] = data["cards_seen"] + 1
    save_progress(data)
    return data["cards_seen"]

# Call this function after a qize is finished

def add_quiz_score(score, total):
    data = load_progress()
    data["quiz_scores"].append({"score": score, "total": total})
    save_progress(data)

# This function make a small text summary for the progress tab

def get_summary():
    data = load_progress()    
    total_quizzes = len(data["quiz_scores"])

    text = "Flashcard viewed: "+ str(data["cards_seen"]) + "\n"
    text = text + "Quize taken: "+ str(total_quizzes)+ "\n"

    if total_quizzes > 0:
        last = data["quiz_scores"][-1]
        text = text + "Last quize score: "+ str(last["score"])+ "/"+ str(last["total"])
    return text