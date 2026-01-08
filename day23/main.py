import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
scoreboard = Scoreboard()

time_count = 0
car = CarManager()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    time_count +=1
    screen.onkey(key="w", fun=turtle.move_up)
    screen.onkey(key="s", fun=turtle.move_down)
    if time_count == 6:
        time_count = 0
        car.create_car()

    car.movecar()
    turtle.check_turtle()
    screen.update()

    #end game if car hits turtle
    for cars in car.cars_list:
        if abs(turtle.ycor() - cars.ycor()) < 15 and cars.xcor() < 25 and cars.xcor() > -25:
            game_is_on = False
            scoreboard.game_over()

    if turtle.ycor() >= 280:
        scoreboard.update_score()
        car.level +=1



screen.exitonclick()