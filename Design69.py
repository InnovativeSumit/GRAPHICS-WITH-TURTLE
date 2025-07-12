from turtle import *
import colorsys as cs
bgcolor('black')
tracer(100)
h,n=0,20
up()
goto(0,0)
down()
pensize(5)
for i in range(250):
    h+=1/n
    color(cs.hsv_to_rgb(h,1,1))
    fd(10)
    circle(i,4.5)
    for j in range(550):
        lt(971)
        circle(i*0.1,j,steps=2)
    circle(i,2)
done()