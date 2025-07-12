from turtle import *
import colorsys as cs

bgcolor('black')
speed(100)
n,h=36,0

for i in range(450):
    h+=1/n
    color(cs.hsv_to_rgb(h,1,1))
    lt(145)
    for j in range(5):
        fd(300)
        towards(150)
done()