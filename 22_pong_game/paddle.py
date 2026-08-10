from turtle import Turtle


class Paddle:
    def __init__(self, x):
        self.x_cord = x
        self.segment = Turtle()
        self.create()

    def create(self):
        t = Turtle()
        t.penup()
        t.color('white')
        t.shape('square')
        t.shapesize(5, 1)
        t.speed('fastest')
        t.goto(self.x_cord - 10, 0)
        self.segment = t

    def move_up(self):
        if self.segment.ycor()<260:
            self.segment.goto(self.segment.xcor(), self.segment.ycor() + 10)

    def move_down(self):
        if self.segment.ycor()>-260:
            self.segment.goto(self.segment.xcor(), self.segment.ycor() - 10)
