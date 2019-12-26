# Symmetric Binary Tree

from turtle import *
mode('logo') # set headings to 0 North, 90 East
pencolor('green') # set pen colour
pen_size = 5 # thickness of the pen
pensize(pen_size) # set pensize
ht() # hide the turtle
iterations = 10 # number of iterations to make
set_speed = 0 # speed of drawing 1 - 10, 10 being fastest, though 0 is faster still
speed(speed = set_speed) # set pen speed
line_length = 200 # determine how long lines are
angle = 60 # angle of the branches
goto(0, -300) # enter a starting position
coordinates = [0, 0, 0] # initiate the coordinates list, x,y and heading

# main outer loop, looping the number of iterations
for i in range(iterations):
    print('Iteration: {}'.format(i)) # prints to shell which iteration

    next_coords = [] # list to hold new coordinates of branch tips, cleared each iteration

    # inner loop, looping through all coordinates
    for i in range(0, len(coordinates), 3):
        # penup, goto coordinates, set heading, pendown, left or right
        # draw branch, plot branch tip coordinates and heading
        pu() 
        goto(coordinates[i], coordinates[i + 1])
        setheading(coordinates[i + 2])
        pd()
        left(angle)
        forward(line_length)
        next_coords.append(xcor())
        next_coords.append(ycor())
        next_coords.append(heading())

        pu()
        goto(coordinates[i], coordinates[i + 1])
        setheading(coordinates[i + 2])
        pd()
        right(angle)
        forward(line_length)
        next_coords.append(xcor())
        next_coords.append(ycor())
        next_coords.append(heading())
    
    coordinates = next_coords # update main coordinates 
    line_length *= 0.61803 # scale line length
    pen_size *= 0.95 # scale pen_size and set
    pensize(pen_size)
