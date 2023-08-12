from turtle import Turtle
import random

COLORS = ["pink", "orange", "yellow", "black", "blue", "purple", "green"]
STARTING_MOVE_DISTANCE = 8


class CarManager:
    def __init__(self, start_x, max_y, speed=STARTING_MOVE_DISTANCE):
        self.speed = speed
        self.start_x = start_x
        self.max_y = max_y
        self.cars = []

    def setup_wave(self):
        no_turtles = random.randint(0, 10)
        for _ in range(no_turtles):
            random_y = random.randint(-self.max_y, self.max_y)
            car = Turtle("square")
            car.penup()
            car.setheading(180)
            car.color(random.choice(COLORS))
            car.goto(self.start_x, random_y)
            self.cars.append(car)

    def move(self):
        to_be_removed = []
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -self.start_x - self.start_x / 5:
                to_be_removed.append(car)
        if to_be_removed:
            self.cars = list(set(self.cars) - set(to_be_removed))

    def get_head_x(self):
        if len(self.cars) > 0:
            return self.cars[0].xcor()
        else:
            return 1

    def check_collision(self, timmy):
        for car in self.cars:
            if car.distance(timmy) < 15:
                return True
        return False

    def reset(self):
        for car in self.cars:
            car.goto(self.start_x * 2, self.max_y * 2)
        self.cars.clear()
        self.__init__(self.start_x, self.max_y)
