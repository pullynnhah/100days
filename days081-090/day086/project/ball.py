from random import choice
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('white')
        self.pu()
        self.move_x = None
        self.move_y = None
        self.set_ball()

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce(self):
        self.move_y *= -1

    def bounce_side_wall(self):
        self.move_x *= -1

    def set_ball(self):
        self.move_x = choice((-5, 5))
        self.move_y = -10

    def reset_position(self):
        self.home()
        self.set_ball()
