from turtle import Turtle

MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self, start_y):
        super().__init__()
        self.start_y = start_y
        self.penup()
        self.goto(0, self.start_y)
        self.shape("turtle")
        self.color("red")
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def reset(self):
        self.goto(0, self.start_y)
