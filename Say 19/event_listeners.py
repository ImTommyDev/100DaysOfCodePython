from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

screen.listen()

#Using an event listener to move the turtle
#When the user presses the "w" key, the turtle moves forward 10 units
#When the user presses the "s" key, the turtle moves backward 10 units
#When the user presses the "a" key, counter-clockwise 10 degrees
#When the user presses the "d" key, clockwise 10 degrees
#When the user presses the "c" key, clear the screen

def move_forward():
    timmy.forward(10)
    
def move_backward():
    timmy.backward(10)
    
def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)
    
def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

#Using the onkey method to bind the keys to the functions
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")


screen.exitonclick()