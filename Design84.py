from turtle import *
import colorsys as cs

bgcolor('black')
tracer(50)
h = 0.4

def draw(ang, n):
    circle(5 + n, 60)
    lt(ang)
    circle(5 + n, 60)

for i in range(200):
    h += 0.005
    color(cs.hsv_to_rgb(h, 1, 1))
    pensize(5)
    draw(90, i * 2)
    draw(120, i * 2.5)

done()