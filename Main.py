from turtle import Screen, Turtle,done
import turtle
import time
from Snake import Snake
from Food import  Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

    

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

scoreboard.update_scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    #Look at last segment and go down to first segment for movement
    snake.move()
    

    #detect collision with food
    if snake.head.distance(food) < 15: 
        food.refresh()
        snake.extend()
        scoreboard.earnpoint()
    
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    #if head collides with any segment of tail trigger game over sequence
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        
    



turtle.done()













screen.exitonclick()
