from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#screen details
screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title("Fun With POGO")
screen.tracer(0)

#objects
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()


# paddle key commands
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor()> 320 or
        ball.distance(l_paddle) < 50 and ball.xcor()< -320):
        ball.bounce_x()

    #detect right paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()

    #detect left paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()








screen.exitonclick()