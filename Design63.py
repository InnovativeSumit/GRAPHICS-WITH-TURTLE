from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
pensize(5)
h=0.7
lt(90)
goto(0,-80)

def tree(x):
    global h
    color(cs.hsv_to_rgb(h,1,1))
    h+=0.03
    if x<10:
        return
    else:
        fd(x)
        lt(30)
        tree(3*x/4)
        rt(60)
        tree(3*x/4)
        lt(30)
        bk(x)

tree(100)
done()