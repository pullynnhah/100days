from turtle import Turtle


class Brick(Turtle):
    def __init__(self, color, pos):
        super().__init__('square')
        self.color(color)
        self.pu()
        self.goto(pos)
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=4)

    def hit(self):
        self.goto(1000, 1000)


class Wall:
    def __init__(self, color, y):
        self.wall = [Brick(color, (x, y)) for x in range(-248, 248, 82)]

    def hit(self, brick):
        self.wall.remove(brick)

    def is_clear(self):
        return len(self.wall) == 0


if __name__ == '__main__':
    from turtle import Screen

    screen = Screen()
    screen.setup(width=800, height=900)
    walls = [Wall(color, pos) for color, pos in [('cyan', 100), ('orchid', 123)]]
    screen.exitonclick()
