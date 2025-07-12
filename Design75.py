from turtle import *
import colorsys as cs

bgcolor('black')
tracer(6)

h=0.4
for i in range(250):
    color(cs.hsv_to_rgb(h,1,1))
    h+=0.005
    width(i//100+3)
    fillcolor(cs.hsv_to_rgb(h,1,1))
    lt(59)
    begin_fill()
    fd(i*0.5)
    circle(i*0.1)
    end_fill()
    rt(90)
    fd(i*1.4)
    circle(i,90)

done()