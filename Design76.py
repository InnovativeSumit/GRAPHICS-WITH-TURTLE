from turtle import *
import colorsys as cs

bgcolor('black')
tracer(10)
h = 0.8

def design(ang, n):
    circle(n * 1.2, 90)
    lt(ang)
    circle(n * 1.2, 90)

for i in range(95):
    pencolor(cs.hsv_to_rgb(h, 0.9, 1))
    design(135, i)
    design(135, i)
    design(90, i)
    design(135, i)
    design(135, i)
    h += 0.005

done()