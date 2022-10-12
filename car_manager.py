from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.make_car()

    def make_car(self):
        random_y = random.randint(-250, 260)
        random_x = random.randint(300, 400)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed(0)
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.setposition(x=random_x, y=random_y)

    def move(self):
        random_y = random.randint(-250, 260)
        random_x = random.randint(300, 600)
        if self.xcor() > -300:
            self.forward(self.move_distance)
        else:
            self.setposition(x=random_x, y=random_y)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
