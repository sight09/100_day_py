from turtle import Turtle, Screen, color
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="make ur bet", prompt="which turtel will win the race ? enter a color: ",)

y_position = [-70,-40, -10, 20, 50, 80]
all_turtels = []


for turtle_index in range(0, 6):
    new_turtel= Turtle(shape="turtle")
    new_turtel.color(colors[turtle_index])
    new_turtel.penup()
    new_turtel.goto(x = -230, y = y_position[turtle_index])
    all_turtels.append(new_turtel)
    
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtel in all_turtels:
        if turtel.xcor() > 230:
            is_race_on = False
            winning_color = turtel.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} is the winner!")
            else:
                print(f"You've lost! the {winning_color} is the winner!")
                
                
                
        rand_distance = random.randint(0, 10)
        turtel.forward(rand_distance)
        
    

screen.exitonclick()