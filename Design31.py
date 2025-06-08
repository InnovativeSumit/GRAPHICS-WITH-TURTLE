from turtle import *
import colorsys
pensize(2)
bgcolor('black')
speed('fastest')
hue=0.0
for i in range(120):
    col=colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue+=0.05
    for j in range(2):
        fd(i*2)
        rt(200)
        lt(10)
        fd(i*2+1)
    rt(120)
hideturtle()
done()