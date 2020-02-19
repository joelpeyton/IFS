# Heighway Dragon Curve

# 6th Feb 2019

# hhttp://ecademy.agnesscott.edu/~lriddle/ifs/ifs.htm

from turtle import *

# set screen to full size for my desktop
setup(1920,1080)

# hide the turtle and set position of pen
hideturtle()
penup()
setpos(300, 0)
pendown()

pattern = ['R'] # initiate the pattern
iterations = 10 # number of iterations to make
set_speed = 0 # speed of drawing 1 - 10, 10 being fastest, though 0 is faster still
speed(speed = set_speed) # set pen speed
line_length = 10 # determine how long lines are
angle = 90 # angle to turn the pen through

# main loop, looping the number of iterations
for i in range(iterations):
    print('Iteration: {}'.format(i)) # prints to shell which iteration

    # alternate pen colour
    if i % 2 == 0:
        pencolor('red')
    else:
        pencolor('blue')
 
    # next iteration is the pattern flipped retrograde
    # swapping each letter and adding the result after a 'R'
    # https://en.wikipedia.org/wiki/Dragon_curve
    
    temp = [] # temporary list to store next pattern
    # loop through pattern swapping each letter
    for i in range(len(pattern)):
        if pattern[i] == 'R':
            temp.append('L')
        else:
            temp.append('R')

    # flip the temp pattern and add this result to a 'R'
    pattern_addition = ['R'] + list(reversed(temp))

    # update existing pattern
    pattern += pattern_addition

    # loop through each pattern addition
    # drawing accordingly
    for i in range(len(pattern_addition)):
        forward(line_length)
        if pattern_addition[i] == 'R':
            right(angle)
        else:
            left(angle)

Screen().exitonclick()
        

    
