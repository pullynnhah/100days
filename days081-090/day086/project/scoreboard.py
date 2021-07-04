from turtle import Turtle

FONT = 'Atari Classic Chunky'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.lives = 5
        self.color("white")
        self.pu()
        self.goto(200, -250)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score}\nLives: {self.lives}', align='center', font=(FONT, 12, 'normal'))

    def point(self):
        self.score += 50
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER" if self.score < 2100 else "YOU WON", align='center', font=(FONT, 36, 'normal'))

    def take_live(self):
        self.lives -= 1
        self.write_score()
