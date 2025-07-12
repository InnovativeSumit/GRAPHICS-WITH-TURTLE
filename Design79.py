from turtle import *
import colorsys as cs
tracer(200)
pensize(3)
h=0
for i in range(600):
    pencolor(cs.hsv_to_rgb(h,1,1))
    begin_fill()
    circle(-20,240)
    rt(59)
    fd(i*0.5)
    circle(20,120)
    lt(120)
    backward(i*0.5)
    h+=0.005
    end_fill()
done()