from turtle import *
import colorsys
bgcolor('black')
speed('fastest')
pensize(3)
hue=0
for i in range(70):
    col=colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue+=0.05
    lt(10)
    for j in range(2):
        fd(200)
        lt(140)
hideturtle()
done()