from turtle import Turtle

STARTING_POSITIONS = [(350,20), (350,0),(350,-20),(350,-40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
#LEFT = 180
#RIGHT = 0

class Paddle():

    def __init__(self):
        self.paddle_segments = []
        self.create_paddle()
        self.snake_head = self.paddle_segments[0]

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        paddle_segment = Turtle("square")
        paddle_segment.penup()
        paddle_segment.color('white')
        paddle_segment.goto(position)
        self.paddle_segments.append(paddle_segment)

    def extend(self):
        self.add_segment(self.paddle_segments[-1].position())

    def move(self):

        for seg_num in range(len(self.paddle_segments)-1, 0,-1):
            new_x = self.paddle_segments[seg_num-1].xcor()
            new_y = self.paddle_segments[seg_num-1].ycor()
            self.paddle_segments[seg_num].goto(new_x,new_y)

        #self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        #if self.snake_head.heading() != DOWN:
        self.snake_head.setheading(UP)

    def down(self):
        #if self.snake_head.heading() != UP:
        self.snake_head.setheading(DOWN)

