from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.car_speed
            new_y = car.ycor()
            car.goto(new_x, new_y)

    def create_car(self):
        create_chance = random.randint(1, 6)
        if create_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(250, random.randrange(-250, 250))
            self.cars.append(new_car)

    def movement_continue(self):
        self.car_speed += MOVE_INCREMENT
