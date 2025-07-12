from turtle import *
import colorsys as cs
bgcolor('black')
tracer(150)
h = 0
goto(-110, 200)
for i in range(400):
    fillcolor(cs.hsv_to_rgb(h, 1, 1))
    color(cs.hsv_to_rgb(h, 1, 1))
    begin_fill()
    lt(119)
    circle(50, 180)
    circle(-50, 180)
    circle(20)
    backward(350 - i)
    end_fill()
    h += 0.005
done()