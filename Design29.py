from turtle import *
import colorsys
pensize(3)
bgcolor('black')
speed('fastest')
hue=0.0
goto(0,-88)
for i in range(200):
    col=colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue+=0.005
    circle(100-i, 90)
    lt(90)
    circle(100-i)
    rt(90)
hideturtle()
done()