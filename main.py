import time
from turtle import *
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("#18122B")
screen.title("My sanke game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()


    for s in snake.snakes:
        if s == snake.head:
            pass
        elif snake.head.distance(s) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()