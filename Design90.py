from turtle import *
import colorsys as cs
speed(0)
bgcolor('black')
h=0.5
pensize(3)
for i in range(200):
    color(cs.hsv_to_rgb(h,1,1))
    h+=0.005
    rt(10)
    for j in range(5):
        fd(i)
        rt(20*5)
        rt(120)
done()