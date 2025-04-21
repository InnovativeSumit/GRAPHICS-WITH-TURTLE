#MAKE BY SUMIT
from turtle import *
import colorsys
bgcolor('black')
speed('fastest')
colors=['violet','green','yellow','orange','red']
for i in range(100):
    pencolor(colors[i%3])
    fd(i*5)
    rt(144)
hideturtle()
done()