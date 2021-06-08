from time import sleep
from turtle import Screen

from paddle import Paddle
from ball import Ball
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("🕹 Pong ️🕹️")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')


game_over = False

while not game_over:
    sleep(0.1)
    screen.update()
    ball.move()
    if not (-280 <= ball.ycor() <= 280):
        ball.bounce_wall()

    if not (-330 <= ball.xcor() <= 330) and (left_paddle.distance(ball) < 50 or right_paddle.distance(ball) < 50):
        ball.bounce_paddle()
screen.exitonclick()
