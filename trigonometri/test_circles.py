from turtle import *

'''
Programmet tegner én blomst.
Skrev denne fila for å få til å tegne blomsten, da den ikke ble riktig i flowers.py første gang
Lærdom:
Dekomponering og isolering i filer er enklere å teste
goto og setheading er lettere å forholde seg til
'''

# TODO: Fristille start heading til parameterverdi (dette påvirker alt posisjonelt i koden)
def flower(x, y, r):
    color("red")
    fillcolor("red")
    penup()
    setheading(0) # egentlig unødvendig
    goto(x, y)
    goto(x, y + r / 2)
    pendown()
    begin_fill() # Hver form må fylles individuelt
    circle(r)  # topp
    end_fill()
    penup()
    goto(x + r / 2, y)
    setheading(270)
    pendown()
    begin_fill()
    circle(r)  # høyre
    end_fill()
    penup()
    goto(x, y - r / 2)
    setheading(180)
    pendown()
    begin_fill()
    circle(r)  # bunn
    end_fill()
    penup()
    goto(x - r / 2, y)
    setheading(90)
    pendown()
    begin_fill()
    circle(r)  # venstre
    end_fill()
    penup()

    goto(x - r, y)
    setheading(270)
    pendown()
    color("yellow")
    fillcolor("yellow")
    begin_fill()
    circle(r)  # center
    end_fill()

speed(0)
flower(100, -44, 40)
penup()
goto(100,-44) # gå til sentrum av blomsten

mainloop()
