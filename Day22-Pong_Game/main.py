from tkinter import scrolledtext
from turtle import Screen, Turtle, distance
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME BY LUIS")
screen.tracer(0) # get rid of the animations thats why we need the the while loop.

paddle_right = Paddle(x=350, y=0)
paddle_left = Paddle(x=-350, y=0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        #bounce
        ball.bounce_y()

    #Detect collision with the right paddel
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_possition()
        scoreboard.pl_point()

    # Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_possition()
        scoreboard.pr_point()

screen.exitonclick()