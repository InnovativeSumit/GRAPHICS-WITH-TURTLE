from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
pensize(2)
h = 0.8

for i in range(200):
    color(cs.hsv_to_rgb(h,1,1))
    h += 0.005
    rt(20)
    for j in range(5):
        fd(i)
        rt(100)
    rt(120)

hideturtle()
done()