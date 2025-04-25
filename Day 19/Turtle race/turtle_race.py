from turtle import Turtle, Screen
import random

#Create a screen object
screen = Screen()
screen.setup(width=500, height=400)

#Asking what color of turtle will win the win
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
user_bet = screen.textinput("Which turtle will win?", "Enter the color of the turtle")

x=-230
y=-100

#Is race on?
is_race_on = False

#Creating a list of turtles
turtles = []

if user_bet:
    is_race_on = True

for color in colors:
    #Create a turtle object
    turtle = Turtle(shape="turtle")
    
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=x,y=y)
    
    y += 30
    
    turtles.append(turtle)


while is_race_on:
    for turtle in turtles:
        #Generate a random distance between 0 and 10
        #Move the turtle forward by that distance
        
        if turtle.xcor() > 230:
            is_race_on = False
            print(f"{turtle.pencolor()} turtle wins!")
            
            if turtle.pencolor() == user_bet:
                print("You win!")
            else:
                print("You lose!")
            
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()