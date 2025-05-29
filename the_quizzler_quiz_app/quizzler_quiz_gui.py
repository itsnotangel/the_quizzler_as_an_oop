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

        self.question_frame = tk.Frame(main_frame)
        self.question_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 12), wraplength=500, justify="left")
        self.question_label.pack(fill=tk.X, pady=10)

        self.score_label = tk.Label(main_frame, text="Score: 0/0", font=("Arial", 12, "bold"), fg="darkred")
        self.score_label.pack(fill=tk.X, pady=(0, 10))

        instruction_label = tk.Label(main_frame, text="Instruction: Select the correct answer from the four choices.", font=("Arial", 10), fg="grey")
        instruction_label.pack(fill=tk.X, pady=(0, 5))

        self.choices_frame = tk.Frame(main_frame)
        self.choices_frame.pack(fill=tk.X, padx=20, pady=10)

        self.choice_buttons = []
        self.choice_labels = ["A", "B", "C", "D"]

        for i in range(4):
            choice_frame = tk.Frame(self.choices_frame)
            choice_frame.pack(fill=tk.X, pady=5)

            button = tk.Button(
                choice_frame,
                text=f"{self.choice_labels[i]}.",
                font=("Arial", 10, "bold"),
                anchor="w",
                width=30,
                fg="darkred",
                command=lambda idx=i: self.check_answer(self.choice_labels[idx])
            )
            button.pack(fill=tk.X)
            self.choice_buttons.append(button)

            self.next_question_button = tk.Button(
            main_frame,
            text="NEXT QUESTION",
            font=("Arial", 10, "bold"),
            fg="black",
            width=15,
            command=self.next_question
        )
        self.next_question_button.pack(side=tk.LEFT, padx=20, pady=(10, 0))

        self.exit_button = tk.Button(
            main_frame,
            text="EXIT QUIZ",
            font=("Arial", 10, "bold"),
            fg="black",
            width=15,
            command=self.root.destroy
        )
        self.exit_button.pack(side=tk.RIGHT, padx=20, pady=(10, 0))

        self.logic.load_questions()

        if self.logic.quiz_questions:
            self.next_question()
        else:
            messagebox.showerror("ERROR!", "There are no questions found. Make sure that you created questions.")
            root.destroy()

    def next_question(self):
        for button in self.choice_buttons:
            button.config(state=tk.NORMAL)

        question = self.logic.get_next_question()

        if question:
            self.question_label.config(text=question.question_text)
            for i in range(4):
                self.choice_buttons[i].config(text=f"{self.choice_labels[i]}. {question.choices[i]}")

            self.score_label.config(text=self.logic.get_score_text())
        else:
            self.question_label.config(text=self.logic.get_final_score_text())
            for button in self.choice_buttons:
                button.config(state=tk.DISABLED)
            self.next_question_button.config(state=tk.DISABLED)

    def check_answer(self, selected_answer):
        correct, correct_answer = self.logic.check_answer(selected_answer)

        if correct:
            messagebox.showinfo("CORRECT!", "You selected the correct answer!")
        else:
            messagebox.showerror("INCORRECT!", f"The correct answer to that is {correct_answer}.")

        for button in self.choice_buttons:
            button.config(state=tk.DISABLED)

        self.score_label.config(text=self.logic.get_score_text())