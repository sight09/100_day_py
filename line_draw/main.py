
from turtle import Turtle, Screen

tin = Turtle()

screen = Screen()

def move_forward():
    tin.forward(10)


def move_backwards():
    tin.backward(10)
    


def turn_left():
    new_heading = tin.heading() + 10
    tin.setheading(new_heading)
    
    
def turn_right():
    new_heading = tin.heading() - 10
    tin.setheading(new_heading)
screen.listen()


def clear():
    tin.clear()
    tin.penup()
    tin.home()
    tin.pendown()

screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()

