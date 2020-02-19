# McWorter's pentigree

# 20th Nov 2018

# pattern uses the L system
# rules of construction f -> +f++f----f--f++f++f-
# https://en.wikipedia.org/wiki/L-system

from turtle import *

# set screen to full size for my desktop
setup(1920, 1080)

# hide the turtle and set position of pen
hideturtle()
penup()
setpos(-600, 200)
pendown()

depth = 4 # how deep to make the recursion
set_speed = 0 # speed of drawing 1 - 10, 10 being fastest, though 0 is faster still
speed(speed = set_speed) # set pen speed
pattern = ['f'] # the axiom or starting value
line_length = 5 # length of line
angle = 36 # angle to turn the pen through
rules= ['+', 'f', '+', '+', 'f', '-', '-', '-', '-', 'f', '-', '-',
        'f', '+', '+', 'f', '+', '+', 'f', '-'] # rules of construction 


def pentigree(depth, pattern):
    current_pattern = []
    if depth >= 0:
        for value in pattern:
            if value == 'f':
                current_pattern += rules
            elif value == '+':
                current_pattern.append('+')
            else:
                current_pattern.append('-')
        
        pentigree(depth - 1, current_pattern)
    else:
        for value in pattern:
            if value == 'f':
                forward(line_length)
            elif value == '+':
                right(angle)
            else:
                left(angle)
        

pentigree(depth, pattern)
Screen().exitonclick()