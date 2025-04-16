#MAKE BY SUMIT 
import turtle as t
t.bgcolor('black')
t.pencolor("white")
t.speed('fastest')
t.pensize(3)
def pen(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def pattern():
    for i in range(23):
        t.forward(360)
        t.fillcolor('magenta')
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        t.left(219)
def star():
    for i in range(9):
        t.forward(80)
        t.left(160)
pen(-180, 100)
pattern()
pen(-40, 30)
star()
pen(-10, -184)
t.circle(220)
pen(-10, -194)
t.circle(230)
pen(-10, -144)
t.circle(180)
pen(-2, -10)
t.circle(46)
t.hideturtle()
t.done()



