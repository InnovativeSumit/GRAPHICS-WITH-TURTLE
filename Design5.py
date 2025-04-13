# MADE BY SUMIT
import turtle
turtle.speed(0)
turtle.setup(700, 630)
turtle.bgcolor('black')
turtle.pencolor('cyan')
turtle.pensize(2)
for j in range(10):
    rad = 150
    for i in range(10):
        turtle.circle(rad)
        rad -= 4
        turtle.right(30)

turtle.hideturtle()
turtle.done()