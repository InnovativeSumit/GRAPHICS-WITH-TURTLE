# MADE BY SUMIT
from turtle import *
import colorsys
bgcolor('black')  
tracer(10)  
hue = 0.0
hideturtle()         
for i in range(470):
    col = colorsys.hsv_to_rgb(hue, 1, 1) 
    pencolor(col)  
    hue += 0.005 
    fd(i)
    rt(160)  

    for j in range(2):
        fd(i)      
        rt(130)     
       
done()
