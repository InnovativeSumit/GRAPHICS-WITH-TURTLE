from turtle import *
import colorsys as cs

bgcolor('black')
h=0
tracer(100)
for i in range(600):
    h+=1/250
    up()
    goto(0,0)
    down()
    color(cs.hsv_to_rgb(h,1,1))
    pensize(7)
    lt(19)
    fd(10)
    for j in range(2,i,200):
        rt(70)
        bk(40)
        circle(i,90,steps=1)
        fd(30)
hideturtle()
done()