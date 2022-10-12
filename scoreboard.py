from turtle import Turtle
FONT = ("Courier", 19, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(x=-290, y=260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
