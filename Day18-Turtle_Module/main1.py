import turtle as t
import random

tor = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tor.speed("fastest")

def draw_spirograph(ang):
    for _ in range(int(360/ang)):
        tor.color(random_color())
        tor.circle(100)
        tor.setheading(tor.heading() + 10)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()