# Koch Curve

# 20th Nov 2018

# pattern uses the L system
# rules of construction f -> f+f--f+f
# hhttp://ecademy.agnesscott.edu/~lriddle/ifs/ifs.htm

from turtle import *

# set screen to full size for my desktop
setup(1920, 1080)

# hide the turtle and set position of pen
hideturtle()
penup()
setpos(-600, -200)
pendown()

depth = 4 # how deep to make the recursion
set_speed = 0 # speed of drawing 1 - 10, 10 being fastest, though 0 is faster still
speed(speed = set_speed) # set pen speed
pattern = ['f'] # the axiom or starting value
line_length = 50 # length of line
angle = 60 # angle to turn the pen through
rules = ['f', '+', 'f', '-', '-', 'f', '+', 'f'] # rules of construction f -> f+f--f+f

def koch_curve(depth, pattern):
    current_pattern = []
    if depth >= 0:
        for value in pattern:
            if value == 'f':
                current_pattern += rules
            elif value == '+':
                current_pattern.append('+')
            else:
                current_pattern.append('-')

        koch_curve(depth - 1, current_pattern)
    else:
        for value in pattern:
            if value == 'f':
                forward(line_length)
            elif value == '+':
                left(angle)
            else:
                right(angle)
        

koch_curve(depth, pattern)
Screen().exitonclick()