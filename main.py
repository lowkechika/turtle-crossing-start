import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


def game_over():
    print("WARNING! Collision detected!")
    turtle.goto(0, 0)
    turtle.color("red")
    turtle.write("GAME OVER", False, font=FONT, align=ALIGNMENT)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

score = Scoreboard()
player = Player()
cars = CarManager()

screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()
    score.display_level()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_over()
            game_is_on = False

        if player.level_up():
            player.refresh_game()
            score.raise_score()
            cars.increase_car_speed()

screen.exitonclick()
