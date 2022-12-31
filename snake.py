from turtle import Turtle

BODY_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20


class Snake:

    def __init__(self):
        self.segment = []
        self.create_initial_body()
        self.head = self.segment[0]

    def create_initial_body(self):
        """Create 3 snake segments"""
        for position in BODY_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segment.append(segment)

    def extend(self):
        self.add_segment(self.segment[-1].pos())

    def move(self):
        snake_len = len(self.segment)
        for index in range(snake_len - 1, 0, -1):
            self.segment[index].goto(self.segment[index - 1].xcor(), self.segment[index - 1].ycor())
        self.head.forward(MOVE_STEP)

    def up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)

    def down(self):
        if self.head.heading() == 0:
            self.head.right(90)
        elif self.head.heading() == 180:
            self.head.left(90)

    def left(self):
        if self.head.heading() == 90:
            self.head.left(90)
        elif self.head.heading() == 270:
            self.head.right(90)

    def right(self):
        if self.head.heading() == 90:
            self.head.right(90)
        elif self.head.heading() == 270:
            self.head.left(90)
