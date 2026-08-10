import random
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

WIDTH = 800
HEIGHT = 600

s = Screen()
s.setup(width=WIDTH, height=HEIGHT)
s.bgcolor('black')
s.title("Pong")
s.tracer(0)

scoreboard = Scoreboard()
paddle_right = Paddle(WIDTH / 2 - 10)
paddle_left = Paddle(-WIDTH / 2 + 20)
ball = Ball()


def handle_up():
    paddle_right.move_up()


def handle_down():
    paddle_right.move_down()


def handle_w():
    paddle_left.move_up()


def handle_s():
    paddle_left.move_down()


s.onkeypress(handle_up, 'Up')
s.onkeypress(handle_down, 'Down')
s.onkeypress(handle_w, 'w')
s.onkeypress(handle_s, 's')


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    s.update()
    s.listen()
    ball.move()

    # ball hitting right paddle
    if ball.xcor() >= 360 and ball.distance(paddle_right.segment) <= 40:
        scoreboard.increment_score_r()
        ball.bounce_on_paddle()
    # ball hitting left paddle
    elif ball.xcor() <= -370 and ball.distance(paddle_left.segment) <= 40:
        scoreboard.increment_score_l()
        ball.bounce_on_paddle()
    elif ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_on_wall()
    # ball hitting the walls
    elif ball.xcor() >= WIDTH/2 - 10 or ball.xcor() <= -WIDTH/2 + 5:
        scoreboard.game_over()
        game_is_on = False


s.exitonclick()
