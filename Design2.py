import turtle

# Create turtle object
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)

# Define colors
colors = ['yellow', 'orange', 'red', 'indigo', 'blue', 'green']

# Drawing loop
for i in range(6):
    t.color(colors[i])
    for j in range(5, 100):
        t.forward(j)
        t.right(60)

t.hideturtle()
turtle.done()
