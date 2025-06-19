from turtle import *

# Setup
bgcolor('black')
speed('fastest')
pencolor('yellow')

# Initial orientation
right(45)

# Drawing loop
for i in range(150):
    circle(30)
    
    if 7 < i < 62:
        left(5)
    elif 80 < i < 113:
        right(5)
        
    if i < 80:
        forward(10)
    else:
        forward(5)

# Finish
hideturtle()
done()
