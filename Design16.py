#MAKE BY SUMIT
from turtle import *
speed('fastest')
color=['cyan','blue','pink','red']
begin_fill()
for i in range(50):
    for j in range(4):
        pencolor(color[i%3])
        fd(2*i*j)
        left(65)
hideturtle()
end_fill()
done()