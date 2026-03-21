from turtle import Screen
import turtle as t
import random


tin = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color
    
    
    
# if the color is given by listed format

# color = ["red", "green", "blue", "black", "yellow", "wheat", "SeaGreen", "purple", "DarkBlue", "DarkRed", "DarkGreen", "DarkMagenta"]



directions = [0, 90, 180, 270]
tin.pensize(15)
tin.speed("fastest")

for _ in range(200):
    
    # tin.color(random.choice(color))   #for listed color
`
    tin.color(random_color())
    tin.forward(30)
    tin.setheading(random.choice(directions))








my_screen = Screen()
my_screen.exitonclick()