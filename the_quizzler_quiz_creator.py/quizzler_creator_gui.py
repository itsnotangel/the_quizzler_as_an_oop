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

        # Creating a main frame for the application
        main_frame = tk.Frame(root, bd=5, relief="groove", padx=20, pady=20)
        main_frame.pack(fill="both", padx=20, pady=20)

        # Adding the main title of the window
        main_title_label = tk.Label(main_frame, text="WELCOME TO THE QUIZZLER", font=("Arial", 18, "bold"), fg="darkred")
        main_title_label.pack(fill=tk.X, pady=(10, 0))

        # Adding an instruction label to guide the user on how to use the application
        instruction = tk.Label(main_frame, text="Enter the question, answer (strictly letters A, B, C, or D), and \nfour choices.", font=("Arial", 10), fg="grey")
        instruction.pack(fill=tk.X, pady=(0, 10))
