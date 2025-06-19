from turtle import *
import colorsys
bgcolor('black')
speed('fastest')
hue,n=0,200
for i in range(200):
    begin_fill()
    for j in range(2):
        col=colorsys.hsv_to_rgb(hue, 1, 1)
        color(col)
        hue += 1/n
        lt(20)
        fd(i-j)
    end_fill()
hideturtle()
done()