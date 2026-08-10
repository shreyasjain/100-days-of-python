import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.create()

    def create(self):
        if random.randint(0, 6) == 6:
            t = Turtle()
            t.color(random.choice(COLORS))
            t.shape("square")
            t.penup()
            t.goto(random.randint(300, 400),random.randint(-250,250))
            t.shapesize(1, 2)
            self.cars.append(t)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.cars_speed)

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT
