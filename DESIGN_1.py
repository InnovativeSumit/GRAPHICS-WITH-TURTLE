from turtle import *

# Setup
t = Turtle()
bgcolor("black")
setup(600, 600)
colormode(255)

# Turtle properties
t.pensize(2)
t.speed(6)

# Define colors
colors = ['turquoise', 'blue', 'teal', 'navy']

# Drawing loop
for i in range(280):
    t.pencolor(colors[i % 4])
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)

t.hideturtle()
mainloop()
