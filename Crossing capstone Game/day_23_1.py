import time
from turtle import Screen
from day_23_2 import Player
from day_23_3 import Objects
from day_23_4 import Scoreboard

window =Screen()

window.bgcolor("black")
window.title("usman capstone game")
window.setup(width=600,height=600)
window.tracer(0)

player=Player()
cars=Objects()
pointer=Scoreboard()

window.listen()
window.onkey(player.upward,"Up")
window.onkey(player.down,"Down")
window.onkey(player.left,"Left")
window.onkey(player.right,"Right")


is_game_on=True
while is_game_on:
    time.sleep(0.1)
    window.update()
    cars.create()
    cars.move()
    if player.ycor()>280:
        pointer.update()# level up display
        player.resets()# turtle come back to it's position
        cars.level_up()


    for item in cars.all_segments:
        if item.distance(player) < 20:
            pointer.ending()
            is_game_on=False



window.exitonclick()