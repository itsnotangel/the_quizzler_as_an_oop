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

    def save_to_file(self):
        # Write all stored questions to the output text file
        with open("data_for_the_quizzler.txt", "w") as file:
            for i, q in enumerate(self.question_answer_choices, 1):
                file.write(f"Question {i}: {q['question']}\n")
                file.write(f"Answer: {q['answer']}\n")
                file.write("Choices:\n")
                choice_labels = ['A', 'B', 'C', 'D']
                for j, choice in enumerate(q['choices']):
                    file.write(f"{choice_labels[j]}: {choice}\n")
                file.write("-" * 30 + "\n\n")