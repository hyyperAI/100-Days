from turtle import Turtle

class Pong(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def up(self):
        y_cor = self.ycor()
        self.goto(self.xcor(),y_cor+20,)
    def down(self):
        y_cor = self.ycor()
        self.goto(self.xcor(),y_cor-20)
