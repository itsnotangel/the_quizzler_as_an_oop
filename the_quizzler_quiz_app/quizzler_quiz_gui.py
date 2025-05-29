import tkinter as tk
from tkinter import messagebox
from quizzler_quiz_logic import QuizzlerQuizLogic

class TheQuizzlerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Quizzler - The Ultimate Quiz Edition")
        self.root.geometry("600x530")

        self.logic = QuizzlerQuizLogic()