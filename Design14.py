#MAKE BY SUMIT
import turtle as t
import colorsys
t.bgcolor('black')
t.pensize(2)
t.speed('fastest')
hue=0.0
for i in range (300):
  col =colorsys.hsv_to_rgb(hue,1,1,)
  t.pencolor(col)
  t.fd(i)
  t.rt(61)
  t.circle(10)
  hue+= 0.010
t.hideturtle()
t.done()