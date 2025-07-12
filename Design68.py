from turtle import *
import colorsys as cs
bgcolor('black')
tracer(100)
pensize(5)
h=0
for i in range(250):
    width(i//100+2)
    pencolor(cs.hsv_to_rgb(h,1,0.8))
    h +=0.006
    rt(120)
    circle(-i*0.5,-180)
    circle(i*0.5,180)
done()