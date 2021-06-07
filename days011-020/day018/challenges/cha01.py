from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

for _ in range(4):
    tim.fd(100)
    tim.lt(90)

screen.exitonclick()
