from turtle import *
import colorsys as cs
speed(0)
pensize(4)
bgcolor('black')
h = 0
for i in range(400):
    pencolor(cs.hsv_to_rgb(h,1,1))
    fd(i)
    rt(100*5)
    h += 0.005
done()