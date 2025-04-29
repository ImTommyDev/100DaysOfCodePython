from turtle import Turtle

MOVE_DISTANCE = 20  # Distance to move the snake
UP = 90  # Up direction
DOWN = 270  # Down direction
LEFT = 180  # Left direction
RIGHT = 0  # Right direction

class Snake:
    
    #Create segments of the snake
    def __init__(self):
        self.segments = []  # Initialize an empty list to store the segments of the snake
        self.create_snake()  # Call the method to create the snake segments
        self.head = self.segments[0]  # Set the head of the snake to the first segment
    
    def create_snake(self):
        
        # Create a snake segment
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(-20 * i,0)
            self.segments.append(segment)
            
    def move(self):
        
        # Get the segments of the snake
        segments = self.segments
        
        for seg_num in range(len(segments) - 1, 0, -1):
            num_x = segments[seg_num - 1].xcor() # Get the x coordinate of the previous segment
            num_y = segments[seg_num - 1].ycor() # Get the y coordinate of the previous segment
            segments[seg_num].goto(num_x, num_y) # Move the current segment to the previous segment's position
            
        self.head.forward(MOVE_DISTANCE)  # Move the first segment forward
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # Set the heading of the first segment to up (90 degrees)
            
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)