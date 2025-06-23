from turtle import *
import colorsys
bgcolor('black')
speed("fastest")
width(1)

def square(x):
    for i in range(4):
        fd(x)
        lt(90)

def shape(x):
    fd(x)
    lt(45)
    fd(x)
    rt(60)
    width(3)
    square(x)
    width(1)
    rt(165)
    fd(x)
    lt(45)
    fd(x)
    h = 0.0
    for i in range(90):
        color(colorsys.hsv_to_rgb(h, 1, 1))
        circle(50, 4)
        rt(90)
        shape(70)
        rt(135)
        h += 0.01
    done()