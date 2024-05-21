from turtle import Turtle
from tkinter import *
from PIL import Image
import imageio

colors = {
    'A': 'brown',
    'B': 'green',
    }


def do_action(turtle: Turtle, action: str,
              line_length: float, angle: float, scale: float,
              stack: list = []):
    if action >= 'A' and action <= 'U':
        if action in colors.keys():
            turtle.color(colors[action])
        turtle.forward(line_length)
        turtle.color('black')
    elif action >= 'a' and action <= 'u':
        turtle.up()
        turtle.forward(line_length)
        turtle.down()
    elif action == '+':
        turtle.left(angle)
    elif action == '-':
        turtle.left(-angle)
    elif action == '|':
        turtle.right(180)
    elif action == '[':
        stack.append((turtle.position(), turtle.heading()))
    elif action == ']':
        if not stack:
            return
        turtle.up()
        pos, a = stack.pop(-1)
        turtle.setposition(pos)
        turtle.setheading(a)
        turtle.down()
    elif action == '>':
        line_length *= scale
    elif action == '<':
        line_length /= scale
    return line_length


def run_turtle(path: str, angle: float = 90.0, step: float = 10.0,
               scale: float = 1.0, pos=(0, 0)):
    if not path:
        return
    t = Turtle()
    t.width(2)
    t.hideturtle()
    t.up()
    t.setheading(90)
    t.speed(0)
    t.setx(pos[0])
    t.sety(pos[1])
    t.down()

    stack = []
    line_length = step
    for char in path:
        line_length = do_action(t, char, line_length,
                                angle, scale, stack)

    t.screen.mainloop()
