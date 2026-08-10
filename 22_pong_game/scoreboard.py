from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_a_score = 0
        self.player_b_score = 0
        self.display()
        self.display_line()

    def display_line(self):
        self.penup()
        self.goto(0, -300)
        self.pencolor("white")
        self.write("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", align="center", font=("Arial", 30, "normal"))
        self.hideturtle()

    def display(self):
        self.clear()
        self.penup()
        self.goto(0,250)
        self.pencolor("white")
        self.write(f"{self.player_a_score}     {self.player_b_score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def increment_score_l(self):
        self.player_a_score += 1
        self.display()

    def increment_score_r(self):
        self.player_b_score += 1
        self.display()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pencolor("white")
        self.write("Game Over.", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()