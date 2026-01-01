from turtle import Turtle, Screen
import random


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_line = -230
turtle_list = []


screen = Screen()
race = False


def create_turtle(num):
    y_cor = -60 + (30 * num)
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[num])
    tim.goto(x=start_line, y=y_cor)
    turtle_list.append(tim)


screen.setup(width=500, height=400)
guess = screen.textinput(
    title="Predict the winner!",
    prompt="Which turtle will win the race? Enter a color: ",
).lower()


# draw finish line
finishline = Turtle()
finishline.penup()
finishline.goto(x=230, y=100)
finishline.pendown()
finishline.goto(x=230, y=-100)
finishline.hideturtle()


for i in range(6):
    create_turtle(i)


if guess:
    race = True


while race:
    for turtle in turtle_list:
        turtle.forward(random.randint(0, 10))
        # code to make red win race for testing
        # color_temp = turtle.pencolor()
        # if color_temp == "red":
        #     turtle.forward(random.randint(0, 10))
        coord = turtle.pos()
        x_cor = coord[0]
        if x_cor >= 210:
            race = False
            turtle_color = turtle.pencolor()

print(f"The {turtle_color} turtle won the race!")
if guess == turtle_color:
    print("You win!")
else:
    print("You lost!")

screen.exitonclick()
