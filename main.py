import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()

screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.move, "Up")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    car_manager.count += 1
    time.sleep(scoreboard.speed)
    screen.update()
    # Creating and moving the car
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            print("Made contact")
            game_is_on = False
            scoreboard.game_over()

    if player.finish_line():
        scoreboard.update_score()
        player.starting_point()


screen.exitonclick()
