from turtle import Turtle


FONT = ("Arial", 100, "normal")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.text = -1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.update()


    def update(self):
        self.text +=1
        self.clear()
        self.write(arg=self.text,font=FONT, align="center")

