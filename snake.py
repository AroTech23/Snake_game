import random
import turtle
from turtle import Turtle

UP=90
DOWN=270
LEFT=180
RIGHT=0

positions_argument=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.original_segment=[]
        self.create_snake()
        self.head=self.original_segment[0]
    def create_snake(self):
        for position in positions_argument:
            self.add_segment(position)

    def add_segment(self,position):

            new_argument = Turtle ("square")
            new_argument.color ("white")
            new_argument.penup ()
            new_argument.goto (position)
            self.original_segment.append(new_argument)
    def reset(self):
        for seg in self.original_segment:
            seg.goto(1000,1000)
        self.original_segment.clear()
        self.create_snake()
        self.head = self.original_segment[0]

    def extend(self):
        self.add_segment(self.original_segment[-1].position())


    def move(self):

            for segment in range (len(self.original_segment) -1,0,-1):
                new_x = self.original_segment[segment - 1].xcor ()
                new_y = self.original_segment[segment - 1].ycor ()
                self.original_segment[segment].goto ( new_x , new_y )
            self.original_segment[0].forward(20)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading () != UP:

            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading () != RIGHT:

            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading () != LEFT:
            self.head.setheading(RIGHT)





