# Pythagoras Tree

# 6th Feb 2019

# http://ecademy.agnesscott.edu/~lriddle/ifs



from turtle import *
from math import sqrt

# set screen to full size for my desktop
setup(1920, 1080)

# set headings to 0 North, 90 East
mode('logo') 

# hide the turtle
ht() 

# set pen speed
set_speed = 0 # speed of drawing 1 - 10, 10 being fastest, though 0 is faster still
speed(speed = set_speed) 

# set angle of branch
angle = 45 


# draw a square
# goto coordinates
# set heading
# set angle
# draw square
# plot coordinates
# repeat n number of depths
def py_tree(branch, side, x_coord, y_coord, direction, line_length, depth):

    if depth < 9:
        pu()
        goto(x_coord, y_coord)
        setheading(direction)
        pd()
        if branch == 'left':       
            if side == 'left':
                left(angle)
                pencolor('red')
                for i in range(4):
                    forward(line_length)
                    if i == 0:
                        left_x_coord = xcor()
                        left_y_coord = ycor()
                        left_heading = heading()
                    if i == 1:
                        right_x_coord = xcor()
                        right_y_coord = ycor()
                        right_heading = heading()
                    right(90)
                branch = 'left'
            else:
                left(angle)
                pencolor('blue')
                for i in range(4):
                    forward(line_length)
                    if i == 0:
                        right_x_coord = xcor()
                        right_y_coord = ycor()
                        right_heading = heading()
                    if i == 1:
                        left_x_coord = xcor()
                        left_y_coord = ycor()
                        left_heading = heading()
                    left(90)
                branch = 'right'
        else:
            if side == 'left':
                right(angle)
                pencolor('red')
                for i in range(4):
                    forward(line_length)
                    if i == 0:
                        left_x_coord = xcor()
                        left_y_coord = ycor()
                        left_heading = heading()
                    if i == 1:
                        right_x_coord = xcor()
                        right_y_coord = ycor()
                        right_heading = heading()
                    right(90)
                branch = 'left'
            else:
                right(angle)
                pencolor('blue')
                for i in range(4):
                    forward(line_length)
                    if i == 0:
                        right_x_coord = xcor()
                        right_y_coord = ycor()
                        right_heading = heading()
                    if i == 1:
                        left_x_coord = xcor()
                        left_y_coord = ycor()
                        left_heading = heading()
                    left(90)
                branch = 'right'
                
        py_tree(branch, 'left', left_x_coord, left_y_coord, left_heading, line_length * (sqrt(2)/2), depth + 1)
        py_tree(branch, 'right', right_x_coord, right_y_coord, right_heading, line_length * (sqrt(2)/2), depth + 1)

py_tree('left', 'left', -100, -400, 45, 200, 0)
