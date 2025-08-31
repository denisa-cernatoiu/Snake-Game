from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

INITIAL_POS = [(0,0), (-20, 0), (-40, 0)]

class Snake:
    
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def add_segment(self, position):
        snake_segment = Turtle()
        snake_segment.shape("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_body.append(snake_segment)

    def create_snake(self):
        for pos in INITIAL_POS:
           self.add_segment(pos)

    def move(self):
        for seg in range(len(self.snake_body)-1, 0, -1):
                new_x = self.snake_body[seg - 1].xcor()
                new_y = self.snake_body[seg - 1].ycor()
                self.snake_body[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
         self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())



