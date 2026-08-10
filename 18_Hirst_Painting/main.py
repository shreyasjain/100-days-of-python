import colorgram
from turtle import Turtle, Screen

t = Turtle()

raw_colors = colorgram.extract('painting.jpg', 10)
colors = []

for color in raw_colors:
    r = int(color.rgb[0])
    g = int(color.rgb[1])
    b = int(color.rgb[2])
    colors.append((r,g,b))

t.speed("fastest")

for row in range(1,10):
    for _ in range(10):
        t.pendown()
        t.begin_fill()
        t.color('red')
        t.circle(10)
        t.end_fill()
        t.penup()
        t.forward(50)

    t.setx(0)
    t.teleport(y=row * 70)


screen = Screen()
screen.exitonclick()