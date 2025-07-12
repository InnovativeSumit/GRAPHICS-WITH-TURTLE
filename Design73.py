from turtle import *
import colorsys as cs

tracer(9)
pensize(2)
h=0.2
bgcolor("black")
lt(180)
fd(250)
lt(180)
lt(180)

for i in range(330):
    color(cs.hsv_to_rgb(h,1,1))
    h+=0.005
    fd(i)
    rt(40)
    fd(500)
    rt(120)

done()