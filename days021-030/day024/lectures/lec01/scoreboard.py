from turtle import Turtle

ALIGNMENT = 'center'
FONT_SCORE = ('Atari Classic Chunky', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.high_score = 0
        self.pu()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', font=FONT_SCORE, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

