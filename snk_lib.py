import turtle

SLEEP_T = 0.1

# Screen
def screen():
    scr = turtle.Screen()
    scr.title("Snake game")
    scr.bgcolor("black")
    scr.setup(width=600, height=480)
    scr.tracer(0)
