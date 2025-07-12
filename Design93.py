from turtle import *
import colorsys as cs

speed(0)
bgcolor('black')
n,h=70,0

for i in range(360):
    h +=1/n
    color(cs.hsv_to_rgb(h,1,0.8))
    lt(1)
    fd(1)
    for i in range(2):
        lt(2)
        circle(10)
done()