import turtle as t
import random

tor = t.Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]
tor.pensize(15)
tor.speed("fast")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(200):
    tor.color(random_color())
    tor.forward(30)
    tor.setheading(random.choice(directions))

tor.done()
