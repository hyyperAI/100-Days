import random
from turtle import Turtle
INCREMENT=10

class Objects(Turtle):
    def __init__(self):
        super().__init__()
        self.all_segments=[]
        self.level_ups=INCREMENT

    def create(self):
        self.hideturtle()
        item=random.randint(0,3)
        if item == 1:
            segment_1=Turtle("square")
            segment_1.shapesize(0.5,1.5)

            segment_1.color("red")
            segment_1.penup()
            y_cor = random.randint(-300, 300)
            segment_1.goto(280,y_cor)
            self.all_segments.append(segment_1)

    def move(self):
        for item in self.all_segments:
            # it_y_cor=self.ycor()
            item.backward(self.level_ups)

    def level_up(self):
        self.level_ups+=5



