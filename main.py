from turtle import Screen
from player import Player
from level import Level
from car import Car
import random
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

player = Player()
level = Level()
car = Car()

screen.listen()
screen.onkey(key="Up", fun=player.move_player)
speed_decrement = 0

game_is_on = True
while game_is_on:
    level.display_level()
    time.sleep(.1)
    screen.update()
    car.create_car()
    car.move_cars()
    # detect collision with car
    for c in car.all_cars:
        if player.distance(c) <= 20:
            game_is_on = False
    # detect when player has reached other side
    if player.ycor() > 280:
        player.reset_position()
        car.car_speed += 5
        level.level += 1

level.display_game_over()

screen.exitonclick()