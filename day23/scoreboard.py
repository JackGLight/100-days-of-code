from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.penup()
        self.goto(-270, 270)
        self.write(arg=f"Level: {self.score}", font=FONT)


    def update_score(self):
        self.score +=1
        self.clear()
        self.write(arg=f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", font=FONT, align="center")


