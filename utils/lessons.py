# This file handels the lessons features
# It loads lessons from data/lessons.json and provides functions for the Gradio.UI

import json
import os

LESSONS_FILE = os.path.join("data", "lessons.json")

# Load all lessons from JSON

def load_lessons():
    if not os.path.exists(LESSONS_FILE):
        return []

    with open(LESSONS_FILE, "r", encoding = "utf-8") as f:
        return json.load(f)

# Get all lessons titels 

def get_lesson_titles():     
    lessons = load_lessons()

    titles = []

    for lesson in lessons:
        titles.append(lesson["title"])

    return titles

# Find lesson by its title 

def get_lesson_bt_title(title):
    lessons = load_lessons()

    for lesson in lessons:
        if lesson["title"] == title:
            return lesson

    return None

# Create readable lesson information 

def format_lesson(title):
    lesson = get_lesson_bt_title(title)

    if lesson is None:
        return "Lesson not found"

    lesson_text = (
        f"#{lesson['title']}\n\n"
        f"**Category:** {lesson['category']}\n\n"
        f"**Language:**{lesson['language']}\n\n"
        f"**Vocabulary:**{len(lesson['vocabulary_ids'])}\n\n"
        f"Vocabulary IDs:\n"
    )

    for vocabulary_id in lesson["vocabulary_ids"]:
        lesson_text += f"- {vocabulary_id}\n"

    return lesson_text
    