from turtle import *
import colorsys as cs

tracer(50)
bgcolor("black")
h=0.3
pensize(3)

for i in range(500):
    color(cs.hsv_to_rgb(h,1,1))
    h +=0.005
    rt(20)
    for j in range(5):
        fd(i)
        rt(100)
        rt(50)
    rt(118)

done()