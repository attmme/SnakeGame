import turtle
import time
import snk_lib

# Screen
scr = turtle.Screen()
snk_lib.screen()

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"
snake.color("green")

# Direction functions
def mUp():
    snake.direction = "up"

def mDown():
    snake.direction = "down"

def mRight():
    snake.direction = "right"

def mLeft():
    snake.direction = "left"

# Movement function
def movement():
    # Up
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    # Down
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    # Right
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

    # Left
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

# Keyboard
scr.listen()
scr.onkeypress(mUp, "Up")
scr.onkeypress(mDown, "Down")
scr.onkeypress(mRight, "Right")
scr.onkeypress(mLeft, "Left")

# Main loop
while True:
    scr.update()
    movement()
    time.sleep(snk_lib.SLEEP_T)
