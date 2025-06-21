from turtle import *
speed(0)
bgcolor('black')
c=['red', 'orange', 'green', 'blue', 'purple']
pensize(5)
for i in range(200):
    color(c[i%5])
    fd(i)
    lt(100)
    fd(i)
    rt(166)
hideturtle()
done()