from turtle import *
speed(0)
tracer(0)
bgcolor('black')
color=('steelblue', 'coral', 'magenta', 'palegreen')
for i in range(600):
    pencolor(color[i%4])
    pensize(2)
    backward(i)
    rt(120)
    circle(60)
    rt(90)
hideturtle()
done()