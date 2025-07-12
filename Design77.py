from turtle import *
bgcolor('black')
pencolor('green')
tracer(10)
for i in range(180):
    circle(190-i,90)
    lt(90)
    circle(190-i,90)
done()