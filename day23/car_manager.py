from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
# and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen 
# (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. 
# If you get stuck, check the video walkthrough in Step 4



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.hideturtle()
        self.level = 1


    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.turtlesize(stretch_len=2, stretch_wid=1)
        y_cor = random.randint(-240, 240)
        new_car.color(random.choice(COLORS))
        new_car.goto(x=300, y=y_cor)
        self.cars_list.append(new_car)

    def movecar(self):
        for car in self.cars_list:
            new_x = car.xcor() - (STARTING_MOVE_DISTANCE + ((self.level - 1) * MOVE_INCREMENT)/2)
            car.goto(new_x, car.ycor())
        
