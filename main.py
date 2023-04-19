# Snake by Michael Griffiths

import time
from snake import Snake
from turtle import Screen
from fruit import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake= Snake() # create the instance of the Snake
food = Food() # create instance of Food

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    time.sleep(0.1)  # adds 0.1 sec delay
    screen.update()  # update screen
    snake.move()
    if snake.head.distance(food)< 15:
        print("yum")
        food.refresh()

screen.exitonclick()
