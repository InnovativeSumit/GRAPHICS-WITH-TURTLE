from turtle import *
import colorsys as cs

def draw(x,y):
    rt(x)
    fd(y)

tracer(5)
fd(100)
bgcolor('black')
width(2)
color('aqua')

for i in range(150):
    fd(i)
    draw(90,i)
    draw(270,i)

done()