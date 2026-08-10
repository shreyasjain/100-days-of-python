# import tkinter
from turtle import Turtle, Screen
import random

t = Turtle()

def rotate_randomly():
    angles = [0,90,180,270]
    t.setheading(random.choice(angles))

def move():
    colors = ["red", "green", "blue", "yellow", "purple"]
    t.color(random.choice(colors))
    t.circle(50)

for _ in range (100):
    # t.width(5)
    t.speed('fastest')
    # rotate_randomly()
    t.right(10)
    move()

# sides = 2
# colors = ["red", "green", "blue", "yellow", "purple"]
#
# while sides <= 10:
#     angle = 360/sides
#     t.color(random.choice(colors))
#     for _ in range(sides):
#         t.forward(50)
#         t.right(angle)
#     sides += 1

# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# for _ in range(20):
#     t.pendown()
#     t.forward(5)
#     t.penup()
#     t.forward(5)

screen = Screen()