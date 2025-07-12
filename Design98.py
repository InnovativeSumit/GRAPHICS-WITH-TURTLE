from turtle import *
import colorsys as cs

bgcolor('black')
tracer(2)
pensize(5)
h=0

def draw(angle,n):
    circle(5+n,60)
    lt(angle)
    circle(5+n,60)

for i in range(100):
    h += 0.008
    pencolor(cs.hsv_to_rgb(h,1,1))
    draw(90,i*0.5)
    draw(160,i*1.2)
    up()
    draw(180,i)
    draw(90,i*2)
    down()

done()