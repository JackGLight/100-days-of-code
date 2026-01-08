from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

line = Turtle()
line.penup()
line.setpos(0, 350)
line.color("white")
line.setheading(270)
while line.ycor() > -400:
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)



r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball()

l_scoreboard = Scoreboard((-150,150))
r_scoreboard = Scoreboard((150, 150))

screen.listen()

screen.onkey(key="Up",fun=r_paddle.paddle_up)
screen.onkey(key="Down",fun=r_paddle.paddle_down)


screen.onkey(key="w",fun=l_paddle.paddle_up)
screen.onkey(key="s",fun=l_paddle.paddle_down)


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_momentum *= -1


    if r_paddle.distance(ball) < 50 and ball.xcor() >= 330 or l_paddle.distance(ball) < 50 and ball.xcor() <= -330:
        ball.x_momentum *= -1
        ball.ballspeed +=1


    if ball.xcor() > 400:
        ball.x_momentum *= -1
        ball.setpos(0,0)
        l_scoreboard.update()
        ball.ballspeed = 10

    if ball.xcor() < -400:
        ball.x_momentum *= -1
        ball.setpos(0,0)
        r_scoreboard.update()
        ball.ballspeed = 10



screen.exitonclick()


