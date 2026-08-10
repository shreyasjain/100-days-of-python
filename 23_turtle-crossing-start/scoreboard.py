from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create()

    def create(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)