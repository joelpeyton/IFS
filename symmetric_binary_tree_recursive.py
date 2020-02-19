# Symmetric Binary Tree - recursive

# 6th Feb 2019

# http://ecademy.agnesscott.edu/~lriddle/ifs

from turtle import *

# set screen to full size for my desktop
setup(1920, 1080)

# set headings to 0 North, 90 East
mode('logo') 

# set pen colour and thickness of pen
pencolor('green') 
pen_size = 5 
pensize(pen_size) 

# hide the turtle
ht() 

# set pen speed
set_speed = 0 # speed of drawing 1 - 10, 10 being fastest, though 0 is faster still
speed(speed = set_speed) 

# angle of the branches
angle = 60 

# starting position and drawing of main trunk
goto(0, -300) 

# recursive function to draw branch
# goto coordinates, set direction and angle then draw line
# line_scale: 0.58 self avoiding, 0.61803 self connecting, 0.65 self overlapping 
# pen_scale for clarity
def binary_tree(x_coord, y_coord, direction, line_length, pen_size, depth, 
    pen_scale = 0.95, line_scale = 0.61803):

    if depth < 10:
        pensize(pen_size)
        pu()
        goto(x_coord, y_coord)
        setheading(direction)
        pd()
        left(angle)
        forward(line_length)
        binary_tree(xcor(), ycor(), heading(), line_length * line_scale,
                    pen_size * pen_scale, depth + 1)

        pu()
        goto(x_coord, y_coord)
        setheading(direction)
        pd()
        right(angle)
        forward(line_length)
        binary_tree(xcor(), ycor(), heading(), line_length * line_scale,
                    pen_size * pen_scale, depth + 1)

binary_tree(0, 0, 0, 200, 5, 0)
Screen().exitonclick()
