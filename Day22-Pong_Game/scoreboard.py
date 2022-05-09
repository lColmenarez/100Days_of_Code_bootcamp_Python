from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pr_score = 0
        self.pl_score = 0
        self.update_scoreboard()

    def update_scoreboard(self): 
        self.clear()
        self.goto(-100, 200)
        self.write(self.pl_score, align="center", font=("Courier", 82, "normal"))
        self.goto(100, 200)
        self.write(self.pr_score, align="center", font=("Courier", 82, "normal"))

    def pl_point(self):
        self.pl_score += 1
        self.update_scoreboard()

    def pr_point(self):
        self.pr_score += 1
        self.update_scoreboard()