from  turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.up_y=10
        self.down_x=10

    def move(self):
        y_cor=self.ycor()+self.up_y
        x_cor=self.xcor()+self.down_x
        self.goto(x_cor,y_cor)

    def reset_position(self):
        self.goto(0,0)
        self.up_y*=-1
        self.down_x*=-1

    def deflect_wall(self):
        self.up_y*=-1
        # self.down_x*=-1

    def deflect_pong(self):
        self.down_x*=-1