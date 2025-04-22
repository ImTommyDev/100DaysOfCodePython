from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("black")

#Drawing a square with dashed lines
timmy_the_turtle.speed(1)
for i in range(4):
    for i in range (5):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()
        
    
    timmy_the_turtle.right(90)



#Drawing different shapes



















screen = Screen()
screen.exitonclick()