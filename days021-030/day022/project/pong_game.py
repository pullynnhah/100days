from turtle import Screen

from paddle import Paddle

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("🕹 Pong ️🕹️")
screen.tracer(0)

right_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

game_over = False

while not game_over:
    screen.update()

screen.exitonclick()
