from turtle import Turtle

class State():
    def __init__(self, name, xcord, ycord):
        self.create(name, xcord, ycord)

    def create(self, name, x, y):
        t= Turtle()
        t.penup()
        t.hideturtle()
        t.color("black")
        t.goto(x, y)
        t.write(name, font=("Arial", 10, "normal"))