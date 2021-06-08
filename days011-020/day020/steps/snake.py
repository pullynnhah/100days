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




