from turtle import *
import colorsys as cs
bgcolor('black')
h =0.5
for i in range(200):
    color(cs.hsv_to_rgb(h,1,1))
    h +=0.005
    rt(20)
    for j in range(5):
        fd(i)
        rt(20*5)
    rt(40)
rt(120)
done()