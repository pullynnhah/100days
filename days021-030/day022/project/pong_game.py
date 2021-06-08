from turtle import Screen

from paddle import Paddle

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("🕹 Pong ️🕹️")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')


game_over = False

while not game_over:
    screen.update()

screen.exitonclick()
