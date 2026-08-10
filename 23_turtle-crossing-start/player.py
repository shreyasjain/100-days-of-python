from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -FINISH_LINE_Y:
            self.backward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)