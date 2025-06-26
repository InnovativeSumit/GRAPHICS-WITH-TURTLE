from turtle import *
import colorsys as cs
setup(800,800)
width(4)
speed("fastest")
bgcolor("black")
def square(x):
    for i in range(3):
        fd(x)
        lt(90)
    fd(x)
for j in range(20):
    for i in range(10):
        color(cs.hsv_to_rgb(i/10,1-j/20,1))
    rt(135)
    square(150-j*4)
    rt(135)
    circle(50,36)
hideturtle()
done()