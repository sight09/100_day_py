from turtle import Screen
import turtle as t
import random


tin = t.Turtle()
color = ["red", "green", "blue", "black", "yellow", "wheat", "SeaGreen", "purple", "DarkBlue", "DarkRed", "DarkGreen", "DarkMagenta"]


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tin.forward(100)
        tin.right(angle)

for shape_side_n in range(3, 11):
    tin.color(random.choice(color))
    draw_shape(shape_side_n)



my_screen = Screen()
my_screen.exitonclick()
