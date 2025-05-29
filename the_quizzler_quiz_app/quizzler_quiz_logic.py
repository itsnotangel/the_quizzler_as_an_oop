import random
from tkinter import messagebox
from quizzler_quiz_question import QuizQuestion
from quizzler_quiz_utilities import load_quiz_questions_from_file

# Handles quiz questions, current state, and scoring
class QuizzlerQuizLogic:
    def __init__(self):
        self.quiz_questions = []
        self.current_question = None
        self.score_count = 0
        self.total_questions = 0

    # Convert loaded data into QuizQuestions
    def load_questions(self):
        raw_questions = load_quiz_questions_from_file()
        self.quiz_questions = [QuizQuestion(q, a, c) for q, a, c in raw_questions]
        self.total_questions = len(self.quiz_questions)

    # Get next random question and remove it from the list
    def get_next_question(self):
        if self.quiz_questions:
            idx = random.randint(0, len(self.quiz_questions) - 1)
            self.current_question = self.quiz_questions.pop(idx)
            return self.current_question
        else:
            self.current_question = None
            return None
        
    # Checks if answer is correct, updates score
    def check_answer(self, selected_answer):
        if self.current_question:
            if selected_answer == self.current_question.answer:
                self.score_count += 1
                return True, self.current_question.answer
            else:
                return False, self.current_question.answer
        return False, None


