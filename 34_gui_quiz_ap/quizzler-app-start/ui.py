import tkinter

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = tkinter.Tk()
        self.window.minsize(300, 500)
        self.window.title("Trivia Quiz App")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.score_label = tkinter.Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text='hello', fill=THEME_COLOR,
                                                     font=("Arial", 20, 'italic'), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_pic = tkinter.PhotoImage(file="images/true.png")
        self.true_btn = tkinter.Button(image=true_pic, highlightthickness=0, command=self.say_true)
        self.true_btn.grid(padx=20, row=2, column=0)

        false_pic = tkinter.PhotoImage(file="images/false.png")
        self.false_btn = tkinter.Button(image=false_pic, highlightthickness=0, command=self.say_false)
        self.false_btn.grid(padx=20, row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached end of questions.")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def reset_bg(self):
        self.canvas.config(bg="white")
        self.get_next_question()

    def say_true(self):
        a = self.quiz.check_answer('True')
        if a:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.reset_bg)

    def say_false(self):
        a = self.quiz.check_answer('False')
        if a:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.reset_bg)
