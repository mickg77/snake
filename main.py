# Snake by Michael Griffiths

import time
from snake import Snake
from turtle import Screen
from fruit import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake= Snake() # create the instance of the Snake
food = Food() # create instance of Food
scoreboard = Scoreboard()

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
        scoreboard.increaseScore()
        food.refresh()
        snake.extend()
    #detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        scoreboard.gameOver()

    #detect collision with tail
    #if head collides with any segment then gameover

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameOver()

screen.exitonclick()
