from time import sleep
from turtle import Screen

from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from wall import Wall

screen = Screen()

screen.setup(width=600, height=900)
screen.bgcolor('black')
screen.title("🕹 Breakout ️🕹️")
screen.tracer(0)

colors = ['cyan', 'orchid', 'royal blue', 'lime green', 'gold', 'orange red']

walls = [Wall(color, position) for color, position in zip(colors, range(200, 430, 23))]
ball = Ball()
paddle = Paddle()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')

while scoreboard.score < 2100:
    sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with color walls
    for pos in range(180, 410, 23):
        for wall in walls:
            for brick in wall.wall:
                if ball.distance(brick) < 40:
                    brick.hit()
                    scoreboard.point()
                    ball.bounce()

    # Detect collision with ceil
    if ball.ycor() >= 340:
        ball.bounce()

    # Detect collision with floor
    if ball.ycor() <= -340:
        scoreboard.take_live()
        if scoreboard.lives == 0:
            break
        paddle.reset_paddle()
        ball.reset_position()

    # Detect collision with paddle
    if ball.ycor() <= -300 and paddle.distance(ball) < 50:
        ball.bounce()

    # Detect collision with side walls
    if not (-280 <= ball.xcor() <= 280):
        ball.bounce_side_wall()

scoreboard.game_over()

screen.exitonclick()
