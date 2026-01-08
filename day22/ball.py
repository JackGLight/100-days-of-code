from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.y_momentum = 1
        self.x_momentum = 1
        self.ballspeed = 10



    def move(self):
        new_x = self.xcor() + (self.ballspeed * self.x_momentum)
        new_y = self.ycor() + (self.ballspeed * self.y_momentum)
        self.goto(new_x, new_y)