class QuizzlerLogic:
    def __init__(self):
        # Create a storage for questions, answers, and choices
        self.question_answer_choices = []

    def add_question(self, question, answer, choices):
        # Store question data as dictionary
        question_answer_choices_data = {
            "question": question,
            "answer": answer,
            "choices": choices
        }
        # Append data to the internal list
        self.question_answer_choices.append(question_answer_choices_data)