from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
s.title("My Snake Game")
s.bgcolor("black")
s.tracer(0)
s.listen()

s.onkey(snake.move_up, "Up")
s.onkey(snake.move_down, "Down")
s.onkey(snake.move_left, "Left")
s.onkey(snake.move_right, "Right")

game_is_on = True

def game_over():
    global game_is_on
    game_is_on = False
    scoreboard.game_over()

while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.enlarge()
        food.refresh()
        scoreboard.increment_score()

    # detect collision with wall
    if snake.edges_touched(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)):
        game_over()

    # detect collision with tail
    if snake.tail_touched():
        game_over()

s.exitonclick()
