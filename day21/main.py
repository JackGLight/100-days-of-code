from turtle import Screen
import time
from snake import Snake
from food import Food
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()

scoreboard = Scoreboard()

food = Food()


screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scored()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
        # game_on = False

    #Detect collision with tail 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # scoreboard.game_over()
            # game_on = False
            scoreboard.reset()
            snake.reset()            

screen.exitonclick()
