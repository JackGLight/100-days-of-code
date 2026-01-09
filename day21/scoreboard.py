from turtle import Turtle

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data.txt"

with open(DATA_PATH) as file:
    hs = int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = hs
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.scored()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align='center', font=('Courier', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            with open(DATA_PATH,mode="w") as file:
                file.write(str(self.score))
        self.high_score = self.score
        self.score = -1
        self.scored()

    def scored(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Courier', 24, 'normal'))