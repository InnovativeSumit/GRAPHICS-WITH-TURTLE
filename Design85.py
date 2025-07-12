from turtle import *
import colorsys as cs
speed(0)
bgcolor('black')
pensize(2)
h=0.2
for i in range(180):
    h += 0.002
    fillcolor(cs.hsv_to_rgb(h,1,1))
    begin_fill()
    circle(180-i,70)
    lt(80)
    circle(180-i,70)
    rt(20)
    for i in range(4):
        rt(60)
        lt(120)
done()