from turtle import *
import colorsys
bgcolor('black')
speed('fastest')
pensize(3)
hue=0.0
for i in range(170):
    col=colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue+=0.05
    fd(i)
    circle(4)
    lt(40)
hideturtle()
done()