# Snake by Michael Griffiths

import time
from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake= Snake()

game_is_on = True

while game_is_on:
    time.sleep(0.1)  # adds 0.1 sec delay
    screen.update()  # update screen
    snake.move()


screen.exitonclick()
