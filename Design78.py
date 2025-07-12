from turtle import *
import colorsys as cs,random as r
bgcolor('black')
tracer(10)
pensize(2)
h=0.3
for i in range(55):
    x = r.randint(0,0)
    y = r.randint(0,0)
    up()
    goto(x,y)
    down()
    size = r.randint(8,250)
    color(cs.hsv_to_rgb(h,1,1))
    fd(size)
    bk(i)
    rt(90)
    h+= 0.005
done()