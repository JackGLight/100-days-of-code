from turtle import Turtle, Screen

import colorgram
import random
from pathlib import Path


IMG_PATH = Path(__file__).parent / "assets" / "pastel_colors.jpeg"
colors = colorgram.extract(str(IMG_PATH), 15)

screen = Screen()
timmy = Turtle()
screen.colormode(255)

timmy.speed(0)


screen.tracer(0)


def draw_row(turt, num):
    for i in range(num):
        turt.fillcolor(random.choice(colors).rgb)
        turt.begin_fill()
        turt.circle(10)
        turt.end_fill()
        screen.update()

        turt.up()
        turt.forward(30)
        turt.down()


def art(turt, num):
    x_col = 0
    for i in range(num):
        draw_row(turt, num)
        position = turt.pos()
        y_pos = position[1]
        turt.up()
        timmy.setpos(0, y_pos + 30)
        turt.down()
        



art(timmy, 8)




screen.exitonclick()