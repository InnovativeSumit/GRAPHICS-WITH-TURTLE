# MAKE BY SUMIT
import turtle
turtle.speed(0)
turtle.bgcolor('black')
turtle.pencolor('orange')
side=0
while side< 501:
    turtle.forward(side/3)
    turtle.right(45)
    side+=2
turtle.hideturtle()
turtle.done()