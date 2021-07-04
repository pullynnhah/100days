from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__('square')
        self.pu()
        self.reset_paddle()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color('white')

    def reset_paddle(self):
        self.goto(0, -320)

    def go_left(self):
        if self.xcor() > -240:
            self.setx(self.xcor() - 30)

    def go_right(self):
        if self.xcor() < 240:
            self.setx(self.xcor() + 30)
