from turtle import *
import colorsys as cs
tracer(4)
width(2)
h=0
bgcolor('black')
goto(0,-80)

def square(x):
    for i in range(4):
        fd(x)
        lt(90)

for i in range(420):
    circle(80,1)
    rt(90)
    color(cs.hsv_to_rgb(h,1,1))
    square(150)
    lt(90)
    h += 0.003

hideturtle()
done()