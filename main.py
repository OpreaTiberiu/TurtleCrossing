from turtle import Screen
from score import Score
from player import Player
from car_manager import CarManager
import time

SCREEN_X = 1600
SCREEN_Y = 1200
OFFSET = 100
WALL_COLLISION_DISTANCE = 10
DISTANCE_TO_STICK = 85
REFRESH_RATE = 0.1

screen = Screen()
screen.setup(SCREEN_X, SCREEN_Y)
screen.bgcolor("gray")
screen.title("Turtle crossing")
screen.tracer(0)

score = Score(SCREEN_Y, OFFSET)

x_coord = SCREEN_X / 2 - OFFSET
y_coord = SCREEN_Y / 2 - OFFSET

timmy = Player(-y_coord)

car_manager = CarManager(x_coord, y_coord - OFFSET)
car_manager.setup_wave()

screen.listen()
screen.onkey(timmy.up, "Up")
screen.onkey(timmy.down, "Down")

game_on = True
cycle = 0
refresh_rate = 0.0001  # set a faster refresh rate until cars pass the turtle
level_refresh_rate_increase = 1
while game_on:
    if cycle % 8 == 0:
        car_manager.setup_wave()
    car_manager.move()

    screen.update()
    time.sleep(refresh_rate)

    if car_manager.check_collision(timmy):
        game_on = False

    if car_manager.get_head_x() < 0:
        refresh_rate = REFRESH_RATE * level_refresh_rate_increase

    if timmy.ycor() >= y_coord - OFFSET / 2:
        timmy.reset()
        car_manager.reset()
        refresh_rate = 0.0001
        level_refresh_rate_increase *= 0.5
        score.update()

    cycle += 1


score.game_over()
screen.exitonclick()
