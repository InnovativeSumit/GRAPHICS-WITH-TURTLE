from turtle import *
import colorsys
pensize(2)
bgcolor('black')
speed('fastest')
hue=0.0
for i in range(400):
    col=colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue+=0.005
    fd(i)
    circle(20, 200)
hideturtle()
done()