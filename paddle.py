from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(350,0)

    # def move(self):
    #     self.forward(MOVE_DISTANCE)

    def up(self):
        #self.setheading(UP)
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def down(self):
        #self.heading(DOWN)
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)

