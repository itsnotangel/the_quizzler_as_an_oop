import tkinter as tk
from tkinter import messagebox
from quizzler_creator_data_logic import QuizzlerLogic

# The Quizzler class definition, which sets up the main app window and specific dimension
class TheQuizzler:
    def __init__(self, root):
        self.root = root
        self.root.title("The Quizzler - The ultimate Quiz in the Making")
        self.root.geometry("500x500")

        self.logic = QuizzlerLogic()
