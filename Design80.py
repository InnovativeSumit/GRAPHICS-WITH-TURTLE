from turtle import *
import colorsys as cs
speed(0)
bgcolor('black')
h=0.1
pensize(4)
for i in range(300):
    for j in range(4):
        fillcolor(cs.hsv_to_rgb(h,1,1))
        h+=0.004
        begin_fill()
        fd(50)
        rt(20)
        fd(40)
        rt(0)
        end_fill()
goto(0.0)
done()