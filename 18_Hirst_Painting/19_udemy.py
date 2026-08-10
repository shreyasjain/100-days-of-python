import random
from turtle import Turtle, Screen

s = Screen()

rainbow_colors = ['violet', 'indigo', 'blue', 'green', 'red', 'cyan', 'magenta']
all_turtles = []

for i in range(7):
    t= Turtle()
    t.penup()
    t.color(rainbow_colors[i])
    t.goto(-200,-150+(i*50))
    t.speed("slow")
    all_turtles.append(t)

race_is_on = True
while race_is_on:
    for turtle in all_turtles:
        step = random.randint(0,20)
        turtle.forward(step)
        if turtle.xcor()>200:
            race_is_on = False
            color = turtle.pencolor()
            print(f"{color} won")

s.exitonclick()
