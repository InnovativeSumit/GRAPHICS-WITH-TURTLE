#MAKE BY SUMIT
from turtle import *
import colorsys
bgcolor('black')
speed('fastest')
hue=0.0
for i in range(350):
 col=colorsys.hsv_to_rgb(hue,1,1)
 pencolor(col)
 fd(i)
 lt(90)
 circle(41)
 
hideturtle()
done()