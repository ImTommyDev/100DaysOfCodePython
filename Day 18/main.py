from turtle import Turtle, Screen
from random import randint 

# Function to generate random colors
def random_color():
    r = randint(0, 255) / 255
    g = randint(0, 255) / 255
    b = randint(0, 255) / 255
    return r, g, b

# Setting up the screen
screen = Screen()
timmy_the_turtle = Turtle()


timmy_the_turtle.shape("turtle")

#Drawing a square with dashed lines
# timmy_the_turtle.speed(1)

# for i in range(4):
#     for i in range (5):
#         timmy_the_turtle.forward(10)
#         timmy_the_turtle.penup()
#         timmy_the_turtle.forward(10)
#         timmy_the_turtle.pendown()
        
    
#     timmy_the_turtle.right(90)

#Drawing different shapes from triangle to decagon
sides = 3

while sides <= 10:
    for i in range(sides):
        timmy_the_turtle.forward(50)
        degrees = 360 / sides
        timmy_the_turtle.right(degrees)
    
    #Changing the color of the turtle
    color = random_color()
    timmy_the_turtle.color(color)    
    
    sides += 1

screen.exitonclick()