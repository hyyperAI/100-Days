from turtle import Turtle

MOVEMENT=10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        # self=Turtle()
        self.shape("turtle")
        # self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -250)
        # self.speed(0)
        self.seth(90)

    def upward(self):
        self.forward(MOVEMENT)

    def down(self):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor - 20 )

    def right(self):
        x_cor=self.xcor()
        self.goto(x_cor+10,self.ycor())

    def left(self):
        x_cor = self.xcor()
        self.goto(x_cor-10, self.ycor())

    def resets(self):
        self.goto(0, -250)


