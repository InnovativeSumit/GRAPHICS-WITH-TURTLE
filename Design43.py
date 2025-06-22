from turtle import *
import colorsys

speed(0)
bgcolor('black')
pensize(3)
h=0.4

for i in range(300):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    fd(i*2)
    rt(121)

hideturtle()
done()