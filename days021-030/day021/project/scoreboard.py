from turtle import Turtle

ALIGNMENT = 'center'
FONT_SCORE = ('Atari Classic Chunky', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0

        self.pu()
        self.color('white')
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        text = f'Score: {self.score}'
        self.write(text, font=FONT_SCORE, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()
