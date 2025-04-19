#MAKE BY SUMIT
import turtle as t
import colorsys
t.bgcolor('black')
t.speed('fastest')
hue=0.0
for i in range (300):
    color=colorsys.hsv_to_rgb(hue,1,1)
    t.pencolor(color)
    hue+=0.005
    t.fd(i)
    t.lt(200)
    t.circle(20)
t.hideturtle()
t.done()
