from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total=0
        self.create()

    def create(self):
        # self=Turtle()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,200)
        self.write(f"LEVEL = {self.total}", False, "center",('Arial',13,'bold'))

    def update(self):
        self.total+=1
        self.clear()
        self.write(f"LEVEL = {self.total}", False, "center", ('Arial', 13, 'bold'))

    def ending(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER",True,"center",('Classic', 17, 'bold'))
