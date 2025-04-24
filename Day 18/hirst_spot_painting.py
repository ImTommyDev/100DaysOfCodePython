import colorgram

colors = colorgram.extract("C://Users//tommy//Desktop//100 days of code//Day 18//dots.jpg", 30)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
    
#Drawing the dots
import turtle as t
import random

# 10 by 10 grid
t.colormode(255)
tim = t.Turtle()
screen = t.Screen()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_dots = 100

for dot_count in range(1, num_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)  # Reset heading to the right
        
screen.exitonclick()