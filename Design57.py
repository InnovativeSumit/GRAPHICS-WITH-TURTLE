from turtle import *
speed('slowest')
bgcolor('black')
penup()
goto(0,-170)
pendown()
color('red')
begin_fill()
pensize(4)
lt(50)
fd(300)
circle(110,200)
rt(142)
circle(110,200)
fd(300)
end_fill()
color('black')
penup()
goto(-80,35)
pendown()
write("""LOVE""", move=False, font=("verdena",50,""))
hideturtle()
done()