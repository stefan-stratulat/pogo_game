from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(350,0)

    #update paddle to go up (key UP)
    def up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    #update paddle to go down(key DOWN)
    def down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)

