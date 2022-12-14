import time
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard
from level import Level
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()

screen.tracer(0)
player = Player()
# scoreboard = Scoreboard()
screen.onkey(player.move, "Up")
car_manager = CarManager()
level = Level()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Creating and moving the car
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            print("Made contact")
            game_is_on = False
            level.game_over()
            level.write_game_over()
            # scoreboard.game_over()

    if player.finish_line():
        # scoreboard.update_score()
        level.level_up()
        player.starting_point()
        car_manager.movement_continue()


screen.exitonclick()
