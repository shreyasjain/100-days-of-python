class QuestionModel:
    def __init__(self, list):
        self.questions = list

    def get_question(self, index):
        question = self.questions[index]
        return question["text"]

    def get_answer(self, index):
        question = self.questions[index]
        return question["answer"]

    def has(self, index):
        return index < len(self.questions)