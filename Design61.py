from turtle import *

# Setup
bgcolor('black')
pensize(2)
speed(0)
lt(90)
penup()
bk(100)
pendown()

# Recursive tree function
def tree(i):
    if i < 10:
        pencolor('orange')  # Leaf color
        dot(5)
        return
    else:
        pencolor('brown')  # Trunk/branch color
        fd(i)
        lt(30)
        tree(3 * i / 4)
        rt(60)
        tree(3 * i / 4)
        lt(30)
        bk(i)

# Initial call
tree(100)
done()
