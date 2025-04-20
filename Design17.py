#MAKE BY SUMIT
from turtle import *
import colorsys
bgcolor('black')
speed('fastest')
hue=0.0
for i in range(100):
    fd(i*5)
    rt(144)
    color(colorsys.hsv_to_rgb(hue,1,1))
    hue+=0.05
hideturtle()
done()