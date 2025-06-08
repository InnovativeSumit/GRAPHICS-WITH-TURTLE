from turtle import *
import colorsys
pensize(3)
bgcolor('black')
speed('fastest')
hue=0.0
for i in range(385):
    col=colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue+=0.005
    circle(190-i, 100)
    lt(90)
    circle(190-i, 100)
    rt(61)
hideturtle()
done()