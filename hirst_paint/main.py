import colorgram
import turtle
import random

# Extract colors
try:
    colors = colorgram.extract('spot.jpg', 30)  # Increase to 30 for more variety
    if not colors:
        print("No colors extracted. Check if 'spot.jpg' is a valid image file.")
    else:
        # Prepare RGB list (skip the first few if they are background colors)
        rgb_list = []
        for color in colors[1:]:  # Skip the first color if it's mostly white/background
            rgb_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
        
        # Set up Turtle
        tim = turtle.Turtle()
        tim.speed("fastest")
        tim.penup()
        tim.hideturtle()
        turtle.colormode(255)
        
        # Starting position
        tim.setheading(225)
        tim.forward(300)
        tim.setheading(0)
        
        # Draw dots in a grid
        number_of_dots = 100
        for dot_count in range(1, number_of_dots + 1):
            tim.dot(20, random.choice(rgb_list))
            tim.forward(50)
            
            if dot_count % 10 == 0:
                tim.setheading(90)
                tim.forward(50)
                tim.setheading(180)
                tim.forward(500)
                tim.setheading(0)
        
        # Keep the window open
        screen = turtle.Screen()
        screen.exitonclick()
        
except FileNotFoundError:
    print("Error: 'spot.jpg' not found in the current directory.")
except ImportError as e:
    print(f"Import error (possibly missing Pillow or Turtle): {e}. Install with 'pip install Pillow'")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
    
    
    
#====us this comand to run this code 

#  C:\Users\HP\AppData\Local\Programs\Python\Python312\python.exe main.py        