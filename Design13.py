#MAKE BY SUMIT
import turtle as t
t.bgcolor('black')
t.speed('fastest')
list=['purple','red','orange']
for i in range (120):
    t.pencolor(list[1%3])
    t.forward(i*4)
    t.right(121)
t.hideturtle()
t.done()