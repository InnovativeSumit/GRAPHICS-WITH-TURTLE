# MADE BY SUMIT
from turtle import *
import colorsys
bgcolor('black')  
pensize(2)        
speed(0)          
hue = 0.0         

for i in range(400):
    col = colorsys.hsv_to_rgb(hue, 1, 1) 
    pencolor(col)  
    hue += 0.005   

    for j in range(2):
        fd(i)      
        rt(30)     
        fd(50)     
        rt(120)    
    
    rt(121)        

tracer(10)         
hideturtle()       
done()             