#MAKE BY SUMIT
from turtle import *
bgcolor('black')
speed('fastest')
pensize(2)
col=['magenta','yellow','cyan']
for i in range (120):
    pencolor(col[1%3])
    for j in range(2):
        fd(i)
        circle(i)
        fd(i)
    rt(120)
hideturtle()
done()