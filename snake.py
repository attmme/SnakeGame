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
snake.direction = "up"

# Food - add with function object
halfX = snk_lib.SCR_WIDTH/2
halfY = snk_lib.SCR_HEIGHT/2

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 0)

# Snake body
snkBody = []

# Block consecutive oposite direction change
blocking = [False, False, False, False]

# Direction function
def mUp():
    if not blocking[0]:
        snake.direction = "up"

    blocking[1] = True
    blocking[2] = blocking[3] = False

def mDown():
    if not blocking[1]:
        snake.direction = "down"

    blocking[0] = True
    blocking[2] = blocking[3] = False

def mRight():
    if not blocking[2]:
        snake.direction = "right"

    blocking[3] = True
    blocking[0] = blocking[1] = False
    
def mLeft():
    if not blocking[3]:
        snake.direction = "left"

    blocking[2] = True
    blocking[0] = blocking[1] = False

# Keyboard
scr.listen()
scr.onkeypress(mUp, "Up")
scr.onkeypress(mDown, "Down")
scr.onkeypress(mRight, "Right")
scr.onkeypress(mLeft, "Left")

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

# Generate snake body function
def genBody():
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

    
# Food eating function
def foodEating():

    # Collision made with food
    if snake.distance(food) < 20:
        # Food spawn inside the screen (with 40 of marge)
        xFood = random.randint(-halfX+40, halfX-40)
        yFood = random.randint(-halfY+40, halfY-40)

        food.goto(xFood, yFood)

        # Each time snake eats, its size will increase
        newBody = turtle.Turtle()
        newBody.speed(0)
        newBody.shape("square")
        newBody.color("grey")
        newBody.penup()

        snkBody.append(newBody)

        # Increase speed
        snk_lib.SLEEP_T -= 0.002

    # Generate snake body
    genBody()

# Collision function
def collision():
    # Collision made with wall
    xWall = halfX-40
    yWall = halfY-40

    if (snake.xcor() > xWall) or (snake.xcor() < -xWall) or (snake.ycor() > yWall) or (snake.ycor() < -yWall):
        gameOver()

    # Collision with any part of its tail
    for i in snkBody:
        if i.distance(snake) < 20:
            gameOver()
    
# Game over function
def gameOver():
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"

        # Clear the body
        for i in snkBody:
            i.goto(snk_lib.SCR_WIDTH, snk_lib.SCR_HEIGHT)
        snkBody.clear()

        # Reset speed
        snk_lib.SLEEP_T = 0.1

# Main loop
while True:
    # Update screen
    scr.update()

    # Execute everytime snake eats
    foodEating()

    # Keyboard movement detection
    movement()

    # If there's a collision with wall or itself, calls game over
    collision()

    # Delay to avoid overspeed
    time.sleep(snk_lib.SLEEP_T)