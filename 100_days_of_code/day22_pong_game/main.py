from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

# 1-Create the screen
# 2-Create and move a paddle
# 3-Create another paddle
# 4-Create the ball and make it move
# 5-Detect collision with wall and bounce
# 6-Detect collision with paddle
# 7-Detect when paddle misses
# 8-Keep score

# 1-Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# 3-Create another paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # 5-Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() # needs bounce

    # 6-Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.ycor() > -320:
        ball.bounce_x()

    # 7-Detect when paddle misses
    # 7a-Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
    # 7b-Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()




screen.exitonclick()