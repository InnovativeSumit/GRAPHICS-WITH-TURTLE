from turtle import *
import colorsys
bgcolor('black')
speed('fastest')
pensize(3)
goto(110,-30)
hue=0.0
for i in range(4250):
    col=colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(col)
    hue+=0.005
    rt(i)
    circle(140,i-89)
    fd(250)
hideturtle()
done()