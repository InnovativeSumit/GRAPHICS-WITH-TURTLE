from turtle import *
import colorsys as cs
bgcolor("black")
tracer(50)
pensize(4)
h=0.5
for i in range(500):
    h+=0.005
    color('black')
    fillcolor(cs.hsv_to_rgb(h,1,1))
    rt(46.5)
    fd(i)
    circle(20,180)
    circle(55,11)
    end_fill()
    fd(100)
done()