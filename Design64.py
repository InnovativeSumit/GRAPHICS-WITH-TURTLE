from turtle import *
import colorsys as cs
tracer(50)
bgcolor('black')
pensize(4)
h=0
goto(35,0)
for i in range(330):
    h +=0.005
    color('black')
    fillcolor(cs.hsv_to_rgb(h,1,1))
    begin_fill()
    rt(46.5)
    fd(i)
    circle(20,180)
    end_fill()
    circle(i,21)
    fd(100)
hideturtle()
done()