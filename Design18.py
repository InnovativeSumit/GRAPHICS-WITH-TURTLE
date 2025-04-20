#MAKE BY SUMIT
from turtle import *
import colorsys
pensize(4)
bgcolor('black')
speed('fastest')
hue=0.0
for i in range(400):
    col=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    fd(i)
    rt(500)
    hue+=0.095
hideturtle()
done()
