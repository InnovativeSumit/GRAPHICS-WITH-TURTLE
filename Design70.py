from turtle import *
import colorsys as cs

bgcolor('black')
tracer(50)
h=1
pensize(4)

def draw(ang,n):
    circle(5+n,60)
    lt(ang)
    circle(5+n,60)

goto(0,0)
for i in range(160):
    h+=0.005
    pencolor(cs.hsv_to_rgb(h,1,1))
    up()
    draw(180,i)
    down()
    draw(180.1)

done()