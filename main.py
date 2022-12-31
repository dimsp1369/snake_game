from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game. Pro")
screen.tracer(0)
screen.listen()

# variables

is_game_on = True
snake = Snake()
food = Food()
score = Score()

# def set_segment_postition(segment):
#     last_segment = snake[-1]
#     last_segment_pos = last_segment.pos()
#     segment.setx(last_segment_pos[0] - 20)
#     return segment
#

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

while is_game_on:
    screen.update()
    time.sleep(0.15)
    snake.move()
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        is_game_on = False
        score.game_over()
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()
    if snake.head.distance(food) < 15:
        food.random_position()
        score.add_score_point()
        snake.extend()

screen.exitonclick()
