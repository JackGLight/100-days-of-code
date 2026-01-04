from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    #creates segment at given coords
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.setpos(position)
        self.segments.append(snake)


    def extend(self):
        self.add_segment(self.segments[-1].position())





    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        if not self.segments[0].heading() == 270:
            self.segments[0].setheading(90)

    def down(self):
        if not self.segments[0].heading() == 90:
            self.segments[0].setheading(270)

    def left(self):
        if not self.segments[0].heading() == 0:
            self.segments[0].setheading(180)

    def right(self):
        if not self.segments[0].heading() == 180:
            self.segments[0].setheading(0)        



