import tkinter as tk
from tkinter import messagebox
from quizzler_quiz_logic import QuizzlerQuizLogic

class TheQuizzlerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Quizzler - The Ultimate Quiz Edition")
        self.root.geometry("600x530")

        self.logic = QuizzlerQuizLogic()

        main_frame = tk.Frame(root, bd=5, relief="groove", padx=20, pady=20)
        main_frame.pack(fill="both", padx=20, pady=20)

        main_title_label = tk.Label(main_frame, text="THE QUIZZLER", font=("Arial", 30, "bold"), fg="darkred")
        main_title_label.pack(fill=tk.X, pady=(10, 0))

        sub_title_label = tk.Label(main_frame, text="THE ULTIMATE QUIZ EDITION", font=("Arial", 20, "bold"), fg="darkred")
        sub_title_label.pack(fill=tk.X, pady=(0, 10))