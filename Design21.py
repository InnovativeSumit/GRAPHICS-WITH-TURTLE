# MADE BY SUMIT
from turtle import *
import colorsys
bgcolor('black')  
pensize(2)        
colormode(1)     
hue = 0.0         
tracer(10)        
for i in range(400):
    col = colorsys.hsv_to_rgb(hue, 1, 1) 
    pencolor(col)  
    hue += 0.005   

    for j in range(2):
        forward(i)      
        right(60)     
        forward(80)     
        right(150)    
    
    right(121)        

hideturtle()       
done()
