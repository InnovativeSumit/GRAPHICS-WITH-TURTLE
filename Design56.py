from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
for i in range(16):
    begin_fill()
    for j in range(10):
        color(cs.hsv_to_rgb(15,j/15,1))
        rt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6,90)
        rt(180)
        circle(40,24)
    end_fill()
hideturtle()
done()