from turtle import *
import colorsys as cs

speed('fastest')
h=0.3
bgcolor('black')

for i in range(60):
    color(cs.hsv_to_rgb(h,1,1))
    h+=0.2
    begin_fill()
    circle(170-i,100)
    lt(90)
    circle(170-i,100)
    rt(90)
    end_fill()

hideturtle()
done()