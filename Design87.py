from turtle import *
import colorsys as cs

pensize(6)
bgcolor('black')
speed(0)
h=0

for i in range(95):
    pencolor(cs.hsv_to_rgb(h,1,1))
    h +=0.005
    for j in range(17):
        fd(0.2*i)
        lt(33/0.01)

done()