from turtle import *
import colorsys as cs

tracer(100)
bgcolor('black')
pensize(3)
h=0

for i in range(200):
    color(cs.hsv_to_rgb(h,1,1))
    h+=0.002
    circle(200-i,100)
    lt(100)
    circle(200-i,100)
    rt(100)
    for j in range(4):
        lt(200)
done()