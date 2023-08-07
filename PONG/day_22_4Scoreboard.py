from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score=0
        self.r_score=0
        self.updates()

    def updates(self):
        self.goto(100, 200)
        self.write(f"Score {self.r_score}", align="center", font="Courier")
        self.goto(-100, 200)
        self.write(f"Score {self.l_score}", align="center", font="Courier")

    def r_p_score(self):
        self.clear()
        self.r_score += 1
        self.updates()


    def l_p_score(self):
        self.clear()
        self.l_score+=1
        self.updates()