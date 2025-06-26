from turtle import *
speed(0)
hideturtle()
bgcolor('black')
color('cyan')
n,p=1, True
penup()
goto(0,-150)
pendown()
while True:
    circle(n)
    if p:
        n-=1
    else:
        n+=1
    if n==0 or n==60:
        p = not p
    lt(1)
    fd(3)