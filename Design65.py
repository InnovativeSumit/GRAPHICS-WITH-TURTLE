from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
h = 0.8
for i in range(60):
    color(cs.hsv_to_rgb(h,1,1))
    h +=0.005
    fd(i)
    rt(20)
    lt(80)
    circle(150)
    fd(40)
hideturtle()
done()