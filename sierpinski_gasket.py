# Sierpinski Gasket

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
setpos(-400, -400)
pendown()

depth = 4 # how deep to make the recursion
set_speed = 0 # speed of drawing 1 - 10, 10 being fastest, though 0 is faster still
speed(speed = set_speed) # set pen speed
pattern = ['f', '-', 'g', '-', 'g'] # the axiom or starting value
line_length = 20 # length of line
angle = 120 # angle to turn the pen through
rules_f = ['f', '-', 'g', '+', 'f', '+', 'g', '-', 'f'] # rules of construction f -> f-g+f+g-f
rules_g = ['g', 'g']

def sierpinski(depth, pattern):
    final_pattern = []
    if depth >= 0:
        for value in pattern:
            if value == 'f':
                final_pattern += rules_f
            elif value == 'g':
                final_pattern += rules_g 
            elif value == '+':
                final_pattern.append('+')
            else:
                final_pattern.append('-')

        sierpinski(depth - 1, final_pattern)
    else:
        for value in pattern:
            if value == 'f' or value == 'g':
                forward(line_length)
            elif value == '+':
                right(angle)
            else:
                left(angle)
                
        

sierpinski(depth, pattern)
Screen().exitonclick()