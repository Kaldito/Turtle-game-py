import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

cars = []
player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    chance = random.randint(1, 100)
    time.sleep(0.1)
    screen.update()
    if chance < 36 and len(cars) < 25:
        cars.append(CarManager())
    for car in cars:
        car.move()

    if player.ycor() > 280:
        scoreboard.update()
        player.respawn()
        for car in cars:
            car.level_up()

    for car in cars:
        if car.ycor() - 15 < player.ycor() < car.ycor() + 15 and player.distance(car) < 20:
            game_is_on = False

scoreboard.game_over()
screen.exitonclick()
