from turtle import *
import colorsys
bgcolor('black')
speed('fastest')
pensize(5)
hue=0
for i in range(160):
    col=colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue+=0.005
    for j in range(2):
        fd(i)
        rt(60)
        fd(135)
        rt(120)
    rt(20)
hideturtle()
done()