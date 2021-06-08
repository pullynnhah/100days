from random import choice
from turtle import Turtle


HEADINGS = [
    {
        'angle': 45,
        'move_x': 10,
        'move_y': 10
    },
    {
        'angle': 135,
        'move_x': -10,
        'move_y': 10
    },
    {
        'angle': 225,
        'move_x': -10,
        'move_y': -10
    },
    {
        'angle': 315,
        'move_x': 10,
        'move_y': -10
    }
]

class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('white')
        self.pu()
        heading_dict = choice(HEADINGS)
        self.seth(heading_dict['angle'])
        self.move_x = heading_dict['move_x']
        self.move_y = heading_dict['move_y']

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_wall(self):
        self.move_y *= -1

    def bounce_paddle(self):
        self.move_x *= -1
