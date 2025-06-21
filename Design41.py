from turtle import *
import colorsys
bgcolor('black')
speed(0)
hue=0.2
for i in range(100):
    c=colorsys.hsv_to_rgb(hue, 1, 1)
    hue+=0.3
    fillcolor(c)
    begin_fill()
    for j in range(1):
        fd(i*2)
        lt(200)
        fd(i*2)
        rt(100)
        for k in range(2):
            rt(65)
    end_fill()
hideturtle()
done()