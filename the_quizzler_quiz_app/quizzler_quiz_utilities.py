# Import messagebox to display error dialogs in case of file issues
from tkinter import messagebox

# Loads quiz questions, answers, and choices from a formatted text file
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

            question_text = lines[0].replace("Question", "", 1).split(":", 1)[1].strip()
            answer = lines[1].split(":", 1)[1].strip()

            choices = []
            for i in range(3, 7):
                if i < len(lines):
                    choice = lines[i].split(":", 1)[1].strip()
                    choices.append(choice)

            if question_text and answer and len(choices) == 4:
                questions.append((question_text, answer, choices))

        return questions

    except FileNotFoundError:
        messagebox.showerror("ERROR!", "Quiz data file not found.")
        return []