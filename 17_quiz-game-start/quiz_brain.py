from question_model import QuestionModel

class QuizBrain:
    def __init__(self, question_list):
        self.current_question = 0
        # self.total_questions = len(question_list)
        self.score = 0
        self.question_list = question_list

    def play(self):
        # while self.current_question < self.total_questions:
        self.ask_questions()
        self.declare_result()

    def ask_questions(self):
        questions = QuestionModel(self.question_list)
        while questions.has(self.current_question):
            current_question = questions.get_question(self.current_question)
            user_answer = str(input(current_question))
            if user_answer.lower() == questions.get_answer(self.current_question).lower():
                self.score += 1
            self.current_question += 1

    def declare_result(self):
        print(f"You have got {self.score} correct answers out of {len(self.question_list)}")