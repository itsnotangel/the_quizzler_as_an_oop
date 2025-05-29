# Define QuizQuestion class to store question text, choices, and correct answer
class QuizQuestion:
    def __init__(self, question_text, answer, choices):
        self.question_text = question_text
        self.answer = answer.upper()  # Store answer in uppercase
        self.choices = choices