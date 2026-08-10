from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.current_score = 0
        with open('data.txt', 'r') as f:
            self.high_score = int(f.read())
        self.goto(0, 250)
        self.pencolor('white')
        self.refresh_score()
        self.hideturtle()

    def increment_score(self):
        self.current_score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        string = f"Score: {str(self.current_score)} High Score: {str(self.high_score)}"
        self.write(string, font=('Arial', 24, 'normal'), align='center')

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', font=('Arial', 24, 'normal'), align='center')

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open('data.txt', 'w') as f:
                f.write(str(self.high_score))
        self.current_score = 0
        self.refresh_score()