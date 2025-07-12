from turtle import *
import colorsys as cs

bgcolor("black")
tracer(50)
h = 0
for i in range(250):
    fillcolor(cs.hsv_to_rgb(h,1,1,))
    hue = 0.004
    begin_fill()
    up()
    fd(i*2)
    down()
    rt(90)
    for j in range(50):
        fd(i)
        rt(144)
    end_fill()
done()