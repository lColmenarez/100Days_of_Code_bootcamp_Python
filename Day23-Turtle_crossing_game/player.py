from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def is_other_side(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
