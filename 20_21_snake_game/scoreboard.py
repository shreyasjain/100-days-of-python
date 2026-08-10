from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.current_score = 0
        self.goto(0, 250)
        self.pencolor('white')
        self.refresh_score()
        self.hideturtle()

    def increment_score(self):
        self.current_score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        string = "Score: " + str(self.current_score)
        self.write(string, font=('Arial', 24, 'normal'), align='center')

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', font=('Arial', 24, 'normal'), align='center')