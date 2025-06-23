from turtle import *
import colorsys

bgcolor('black')
pensize(2)
speed('fastest')

for j in range(25):
    for i in range(15):
        c=colorsys.hsv_to_rgb(i/15,j/25,1)
        color(c)
        rt(90)
        circle(150-j*4,90)
        lt(90)
        circle(150-j*4,90)
        rt(180)
        circle(50,24)

hideturtle()
done()