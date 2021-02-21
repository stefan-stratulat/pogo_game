from turtle import Screen
from paddle import Paddle

#screen details
screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title("Fun With POGO")

paddle = Paddle()

# paddle key commands
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")









screen.exitonclick()