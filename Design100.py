from turtle import *
import colorsys as cs

bgcolor('black')
tracer(400)
pensize(3)
h=0
goto(-300,200)

for i in range(700):
    color(cs.hsv_to_rgb(h,1,1))
    begin_fill()
    lt(119)
    fd(i*0.5)
    circle(10)
    lt(5)
    backward(600-i*0.7)
    end_fill()
    h +=0.005

done()