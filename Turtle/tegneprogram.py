from turtle import *

def f():
    forward(10)

def b():
    back(10)

def h():
    right(90)

def v():
    left(90)

def p():
    if isdown()==True:
        penup()
    else:
        pendown()

screen = Screen() # Setup for å bruke onclick
listen() # turtlevinduet lytter etter interaksjon

onkeyrelease(f, "Up") # Uten invoke-tegn
onkeyrelease(b,"Down")
onkeyrelease(h, "Right")
onkeyrelease(v, "Left")
onkeyrelease(p, "space") # Toggle pen up pen down
onkeyrelease(clear, "c") # Klikk på c tømmer arket

screen.onclick(goto) # Turtle går dit du klikker

mainloop()