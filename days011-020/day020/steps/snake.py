from turtle import Turtle


class Snake:
    STARTING_POS = ((0, 0), (-20, 0), (-40, 0))
    MOVE_DISTANCE = 20

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in self.STARTING_POS:
            self.segments.append(Turtle('square'))
            self.segments[-1].color('white')
            self.segments[-1].pu()
            self.segments[-1].goto(pos)

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            pos = self.segments[idx - 1].pos()
            self.segments[idx].goto(pos)
        self.head.fd(self.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)





