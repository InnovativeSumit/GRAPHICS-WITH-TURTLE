# MAKE BY SUMIT
from turtle import *
import colorsys

pensize(3)
bgcolor('black')
speed('fastest')
hue = 0.0

for i in range(60):
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue += 0.005  
    for j in range(2):
        forward(i)  # scaled up to make the pattern more visible
        right(60)
        forward(210)
        right(120)

    right(60)
hideturtle()
done()
