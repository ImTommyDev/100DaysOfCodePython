from turtle import Turtle, Screen
from random import randint 

# Function to generate random colors
def random_color():
    r = randint(0, 255) / 255
    g = randint(0, 255) / 255
    b = randint(0, 255) / 255
    return r, g, b

timy_the_turtle = Turtle()
timy_the_turtle.shape("turtle")
timy_the_turtle.speed("fastest")

screen = Screen()

for _ in range(72):
    timy_the_turtle.color(random_color())
    timy_the_turtle.circle(100)
    timy_the_turtle.setheading(timy_the_turtle.heading() + 5)




screen.exitonclick()