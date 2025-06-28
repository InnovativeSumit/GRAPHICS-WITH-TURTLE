from turtle import *
import colorsys as cs
bgcolor("black")
speed("fastest")
h=0
for i in range(500):
    width(i//200+1)
    fillcolor(cs.hsv_to_rgb(h,0.8,1))
    lt(90)
    rt(60)
    begin_fill()
    circle(-i*0.3,70)
    end_fill()
    h += 0.006
done()