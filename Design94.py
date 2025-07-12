from turtle import *
bgcolor("black")
speed(10)
pensize(5)
goto(-300,0)
for i in range(10):
    c=['yellow','violet']
    color(c[i%2])
    begin_fill()
    for j in range(4):
        rt(109)
        circle(140,-100)
    rt(10)
    lt(90)
    end_fill()
done()