from turtle import *
import colorsys as cs

speed("fastest")
h=0.1
bgcolor('black')
pensize(2)
goto(90,-50)
for i in range(200):
    color(cs.hsv_to_rgb(h,1,1))
    h +=0.004
    for j in range(2):
        fd(i/7)
        circle(100,40)
        lt(20)
        circle(100,40)
    rt(120)
hideturtle()
done()