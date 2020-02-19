# Box fractal

# 20th Nov 2018

# pattern uses the L system
# rules of construction f -> f-f+f+f-f
# http://ecademy.agnesscott.edu/~lriddle/ifs

from turtle import *

# set screen to full size for my desktop
setup(1920, 1080)

# hide the turtle and set position of pen
hideturtle()
penup()
setpos(-450, -400)
pendown()

depth = 3 # how deep to make the recursion
set_speed = 0 # speed of drawing 1 - 10, 10 being fastest, though 0 is faster still
speed(speed = set_speed) # set pen speed
pattern = ['f', '-', 'f', '-', 'f', '-', 'f'] # the axiom or starting value
line_length = 10 # length of line
angle = 90 # angle to turn the pen through
rules = ['f', '-', 'f', '+', 'f', '+', 'f', '-', 'f'] # rules of construction f -> f-f+f+f-f



def box_fractal(depth, pattern):
    final_pattern = []
    if depth >= 0:
        for value in pattern:
            if value == 'f':
                final_pattern += rules
            elif value == '+':
                final_pattern.append('+')
            else:
                final_pattern.append('-')

        box_fractal(depth - 1, final_pattern)
    else:
        for value in pattern:
            if value == 'f':
                forward(line_length)
            elif value == '+':
                right(angle)
            else:
                left(angle)  

box_fractal(depth, pattern)
Screen().exitonclick()
