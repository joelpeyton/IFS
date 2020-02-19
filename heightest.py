# Sierpinski Arrowhead Curve

# 20th Nov 2018

# pattern uses the L system
# rules of construction (f -> f-g+f+g-f) (g -> gg)
# https://en.wikipedia.org/wiki/L-system

from turtle import *

# set screen to full size for my desktop
setup(1920, 1080)

# hide the turtle and set position of pen
hideturtle()
penup()
setpos(0, -200)
pendown()

depth = 13 # how deep to make the recursion
set_speed = 0 # speed of drawing 1 - 10, 10 being fastest, though 0 is faster still
speed(speed = set_speed) # set pen speed
pattern = ['f', 'x'] # the axiom or starting value
line_length = 5 # length of line
angle = 45 # angle to turn the pen through
rules_x = ['+', 'f', 'x', '-', '-', 'f', 'y', '+'] # rules of construction a -> b-a-b
rules_y = ['-', 'f', 'x', '+', '+', 'f', 'y', '-'] # rules of construction b -> a-b-a


def sierpinski(depth, pattern):
    final_pattern = []
    if depth >= 0:
        for value in pattern:
            if value == 'f':
                final_pattern.append('z')
            elif value == 'x':
                final_pattern += rules_x
            elif value == 'y':
                final_pattern += rules_y
            elif value == '+':
                final_pattern.append('+')
            elif value == '-':
                final_pattern.append('-')

        sierpinski(depth - 1, final_pattern)
    else:
        for value in pattern:
            if value == 'f':
                forward(line_length)
            elif value == '+':
                left(angle)
            elif value == '-':
                right(angle)
                
sierpinski(depth, pattern)

