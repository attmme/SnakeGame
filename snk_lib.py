import turtle

SLEEP_T = 0.1
SCR_WIDTH = 600
SCR_HEIGHT = 480

# Screen
def screen():
    scr = turtle.Screen()
    scr.title("Snake game")
    scr.bgcolor("black")
    scr.setup(width=SCR_WIDTH, height=SCR_HEIGHT)
    scr.tracer(0)
