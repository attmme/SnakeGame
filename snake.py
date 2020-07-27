import turtle
import time
import snk_lib
import random

# Screen
scr = turtle.Screen()
snk_lib.screen()

# Snake - add with function object
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Food - add with function object
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,0)

# Snake body
snkBody = []


## FUNCTIONS ##

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

# Colision function
def colision():

    # Colision made with food
    if snake.distance(food) < 20:
        halfX = snk_lib.SCR_WIDTH/2
        halfY = snk_lib.SCR_HEIGHT/2

        # Food spawn inside the screen (with 40 of marge)
        x = random.randint(-halfX+40, halfX-40)
        y = random.randint(-halfY+40, halfY-40)
        food.goto(x, y)

        # Each time snake eats, its size will increase
        newBody = turtle.Turtle()
        newBody.speed(0)
        newBody.shape("square")
        newBody.color("grey")
        newBody.penup()

        snkBody.append(newBody)

    # Snake body add and movement animation
    totalBody = len(snkBody)

    # Generate body from the end of the tail to the start
    for i in range(totalBody-1, 0, -1):
        x = snkBody[i-1].xcor()
        y = snkBody[i-1].ycor()
        
        snkBody[i].goto(x, y)

    # Set the first body part just after the 'head'
    if totalBody > 0:
        snkBody[0].goto(snake.xcor(), snake.ycor()) 
        
    # Colision made with wall or itself
    # gameover


# Keyboard
scr.listen()
scr.onkeypress(mUp, "Up")
scr.onkeypress(mDown, "Down")
scr.onkeypress(mRight, "Right")
scr.onkeypress(mLeft, "Left")

# Main loop
while True:
    # Update screen
    scr.update()

    # Check if there's a colision
    colision()

    # Keyboard movement detection
    movement()

    # Delay to avoid overspeed
    time.sleep(snk_lib.SLEEP_T)