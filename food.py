from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.change_pos()

    def change_pos(self):
        random_X = random.randint(-280,280)
        random_Y = random.randint(-280,280)
        self.goto(random_X,random_Y)

