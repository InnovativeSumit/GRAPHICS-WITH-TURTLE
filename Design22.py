#MAKE BY SUMIT
from turtle import *
import colorsys
bgcolor('black')
speed('fastest')
pensize(3)
hue=0.0
for i in range(150):
    col=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    hue+=0.005
    lt(45)
    circle(i)

hideturtle()
done()