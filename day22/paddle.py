from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(start_pos)



    def paddle_up(self):
        paddle_y = self.ycor()
        self.goto(self.xcor(), y=paddle_y + 20)


    def paddle_down(self):
        paddle_y = self.ycor()
        self.goto(self.xcor(), y=paddle_y - 20)