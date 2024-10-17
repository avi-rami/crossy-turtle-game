from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple", "yellow"]
START_MOVE_DISTANCE = 5

class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = START_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,4)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.setheading(180)
            car.setpos(320, random_y)
            self.all_cars.append(car)

    def move_cars(self):
        # keep moving car if it hasn't reached -320x
        for car in self.all_cars:
            if car.xcor() > -320:
                car.forward(self.car_speed)
            # remove car from list if it's no longer moving/visible
            if car.xcor() < -360:
                self.all_cars.remove(car)
