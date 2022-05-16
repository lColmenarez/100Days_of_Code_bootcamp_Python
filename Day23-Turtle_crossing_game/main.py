import time
from turtle import Screen
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("CROSSING GAME BY LUIS")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_cars()
    car_manager.cars_mov()

    #Detect the collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            

    #Detect when the Turlte reach the other side
    if player.is_other_side():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()



screen.exitonclick()