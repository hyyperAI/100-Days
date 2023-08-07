from turtle import Screen
from day_22_2Pong import Pong
from day_22_3ball import Ball
from day_22_4Scoreboard import ScoreBoard
import time
TIME=0.1
window=Screen()
window.bgcolor("black")
window.setup(width=800,height=600)
window.title("PONG By Usman")

# ball=Ball()
window.tracer(0)
# working on pong1

pong_r=Pong((380,0))
pong_l=Pong((-380,0))
ball=Ball()
score_board=ScoreBoard()
# working on functions

window.listen()
window.onkey(pong_r.up,"Up")
window.onkey(pong_r.down,"Down")
window.onkey(pong_l.down,"s")
window.onkey(pong_l.up,"w")

is_game_on=True
while is_game_on:
    time.sleep(TIME)
    window.update()
    ball.move()

    # detect collision with wall
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.deflect_wall()

    # detect collision with pong

    if ball.xcor()==360 and ball.distance(pong_r) <= 50 or ball.xcor()==-360 and ball.distance(pong_l)<=50:
        ball.deflect_pong()
        TIME*=0.9

    #dectect collision of ball to wall
    elif ball.xcor() > 380 :
        score_board.l_p_score()
        ball.reset_position()
        TIME=0.1


    elif ball.xcor() < -380:
        score_board.r_p_score()
        ball.reset_position()
        TIME=0.1

window.exitonclick()