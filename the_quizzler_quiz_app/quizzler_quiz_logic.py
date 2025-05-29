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