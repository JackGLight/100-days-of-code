import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.speed("fastest")
writer.hideturtle()

states = pd.read_csv("50_states.csv")
answered = []
not_answered = states["state"].to_list()
answered_num = int(len(answered))

while answered_num < 50:

    
    answer_state = screen.textinput(title=f"Guess a state ({answered_num}/50)", prompt="What's another state?").title()


    if answer_state == "Exit":
        practice = pd.DataFrame(data=not_answered)
        practice.to_csv("states_to_practice.csv")
        break


    elif states["state"].isin([answer_state.title()]).any() and not answer_state in answered:
        answered.append(answer_state)
        not_answered.remove(answer_state)
        answered_num = int(len(answered))
        x_cor = states["x"][states["state"] == answer_state]
        x = x_cor.iloc[0]
        y_cor = states["y"][states["state"] == answer_state]
        y = y_cor.iloc[0]
        writer.goto(x, y)
        writer.write(f"{answer_state}")



FONT = ("Arial", 64, "normal")
writer.goto(-150,0)
if answered_num == 50:
    writer.write(arg="You Win!", font=FONT)
else:
    writer.goto(-250,0)
    writer.write(arg="Thanks for playing!", font=FONT)



screen.exitonclick()