from turtle import *
import colorsys as cs
bgcolor('black')
h=0
tracer(30)
for i in range(700):
    width(i/100 +1)
    pencolor(cs.hsv_to_rgb(h,1,0.9))
    color(cs.hsv_to_rgb(h,1,0.9))
    left(1000)
    pu()
    fd(i)
    rt(200)
    fd(i)
    rt(120)
    lt(120)
    fd(i)
    fd(i)
    lt(120)
    fd(i)
    pd()
    fd(7)
    rt(10)
    h+=0.002
done()