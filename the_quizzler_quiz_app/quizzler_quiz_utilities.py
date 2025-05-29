from tkinter import messagebox

def load_quiz_questions_from_file(filename="data_for_the_quizzler.txt"):
    try:
        with open(filename, "r") as file:
            content = file.read()
