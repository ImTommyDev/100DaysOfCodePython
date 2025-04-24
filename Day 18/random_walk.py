from turtle import Turtle, Screen
from random import randint 

#create a turtle object
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

screen = Screen()

#Function to generate random colors
def random_color():
    r = randint(0, 255) / 255
    g = randint(0, 255) / 255
    b = randint(0, 255) / 255
    return r, g, b

timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(50):
    timmy_the_turtle.forward(50)
    
    color = random_color()
    timmy_the_turtle.color(color)
    
    #Changing the direction of the turtle
    timmy_the_turtle.setheading(randint(0, 3) * 90)

screen.exitonclick()