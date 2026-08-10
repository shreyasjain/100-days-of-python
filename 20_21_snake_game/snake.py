from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for cordinate in STARTING_POSITIONS:
            self.add_segment(cordinate)

    def enlarge(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        t = Turtle()
        t.penup()
        t.shape("square")
        t.color("white")
        t.turtlesize(1)
        t.goto(position)
        self.segments.append(t)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            prev_segment_position = self.segments[i - 1].position()
            self.segments[i].goto(prev_segment_position)

        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def edges_touched(self, edgex, edgey):
        return (self.head.xcor()>=edgex or self.head.ycor()>=edgey or
                self.head.xcor()<=-edgex or self.head.ycor()<=-edgey)

    def tail_touched(self):
        for segment in self.segments[1:]:
            if segment.position() == self.head.position():
                return True
        return False
