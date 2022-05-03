from turtle import Turtle, Screen, exitonclick, onkey

tor = Turtle()
screen = Screen()

def move_forwards():
    tor.forward(10)

def move_backwards():
    tor.backward(10)

def move_left():
    tor.left(10)

def move_right():
    tor.right(10)

def clear():
    tor.clear()
    tor.penup()
    tor.home()
    tor.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")

screen.exitonclick() 

