from tkinter import messagebox

def load_quiz_questions_from_file(filename="data_for_the_quizzler.txt"):
    try:
        with open(filename, "r") as file:
            content = file.read()
        sections = content.split("-" * 30)
        questions = []

        for section in sections:
            if not section.strip():
                continue

            lines = section.strip().split("\n")
            if len(lines) < 7:
                continue
