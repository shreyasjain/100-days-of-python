import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        # self.heading_angle = random.randint(0, 360)
        # self.heading_angle = 175
        self.x_move = 10
        self.y_move = 10

    def create(self):
        self.color("white")
        self.penup()
        self.shape('circle')

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.setheading(self.heading_angle)
        # self.forward(10)

    def bounce_on_wall(self):
        self.y_move *= -1
        # self.heading_angle = 360 - self.heading()
        # self.forward(10)

    def bounce_on_paddle(self):
        self.x_move *= -1
        # if self.heading_angle <=180:
        #     self.heading_angle = self.heading_angle - 90
        #     self.forward(10)
        # else :
        #     self.heading_angle = self.heading_angle + 90
        #     self.forward(10)
