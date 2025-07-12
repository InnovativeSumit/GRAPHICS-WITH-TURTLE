from turtle import *
import colorsys as cs
tracer(6)
bgcolor('black')
h=0.3
goto(0,120)
for i in range(190):
    fillcolor(cs.hsv_to_rgb(h,1,1))
    h+=0.005
    begin_fill()
    circle(190-i,90)
    lt(90)
    lt(20)
    circle(190-i,90)
    lt(18)
    end_fill()
done()