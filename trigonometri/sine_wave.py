import turtle
from turtle import *
import math

#initialize
shape("turtle")
speed(0)
turtle.Screen().setworldcoordinates(0,-1.1,math.tau,1.1) # Forskjellig ved grader og radianer

t = math.tau
angle = 0 # Startverdi i while-løkka både for radianer og grader

penup()
goto(0,0)
pendown()

# turtle.Screen().setworldcoordinates(0,-1.1,360,1.1)
# while angle <= 360:
#     goto(angle,math.sin(math.radians(angle)))
#     angle += 0.1
#
while angle <= math.tau:
    goto(angle, math.sin(angle))
    angle += 0.01