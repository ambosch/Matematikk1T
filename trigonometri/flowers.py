from turtle import *
import random as rm

# Programmet tegner en randomisert blomstereng
# Enhentssirkelen må forstås for å tegne blomstene riktig

'''
Ressurser å utforske videre
https://realpython.com/beginners-guide-python-turtle/
https://direct.mit.edu/books/book/4663/Turtle-GeometryThe-Computer-as-a-Medium-for
https://processing.org/books/
https://processing.org/tutorials/trig
https://oppgaver.kidsakoder.no/processing/trigonometri/README
'''

# Oppsett av bakgrunnen
screen = Screen()
screen.setup(1050,450) # Setter vindustørrelse (inkludert topp, og bunnmarg)
#screensize(1000 ,400) # Setter tegningstørrelse ikke sikker hva jeg skal gjøre med denne enda
bgcolor("seagreen")
speed(0) # 0 er raskeste fart, 1 er sakteste fart
shape("turtle")
colormode(255) # RGB
#color("black")
#fillcolor("saddlebrown") # Henter fra CSS colors her https://www.w3schools.com/cssref/css_colors.asp

# Egne variabler for generalisering og gjenbruk av kode
hoyre_kant = window_width()/2
venstre_kant = -hoyre_kant
topp_kant = window_height()/2
bunn_kant = -topp_kant

def triangle(x,y,step, triangle_color="saddlebrown"): # Valgfri parameter farge
    penup()
    goto(x,y)
    color(triangle_color)
    fillcolor(triangle_color)
    pendown()
    begin_fill()
    for i in range(3): # Tegner en trekant
        forward(step)
        right(120) # ytre vinkel = 180 - 30 grader
    end_fill()
    penup()


def flower_old(x,y, r): # Denne funker ikke som den skal, den gule sirkelen er ikke riktig. Sett head og posisjon matematisk
    color("red")
    fillcolor("red")
    penup()
    goto(x,y+r)
    for i in range(4):
        penup()
        back(r)
        pendown()
        begin_fill()
        circle(r)
        end_fill()
        right(90)
    penup() # Nå peker head inn mot blomsten
    right(90)
    forward(r+r/2)
    left(90)
    back(r/2)
    color("yellow")
    fillcolor("yellow")
    pendown()
    begin_fill()
    circle(r)
    end_fill()
    penup()

# TODO: Fristille start heading til parameterverdi (dette påvirker alt posisjonelt i koden)
def flower(x, y, r, color_r,color_g,color_b):
    pencolor(color_r, color_g, color_b)
    fillcolor(color_r, color_g, color_b)
    #color("red")
    #fillcolor("red")
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
    pencolor(color_r, color_g, color_b)
    fillcolor(color_r, color_g, color_b)

def n_flowers(n):
    for i in range(n):
        # randomiserer farge
        color_r = rm.randint(0, 255)
        color_g = rm.randint(0, 255)
        color_b = rm.randint(0, 255)

        #randomiserer radius
        r = rm.randint(5,55)

        # randomiserer posisjon
        x = rm.randint(venstre_kant,hoyre_kant)
        y = rm.randint(bunn_kant,topp_kant)
        flower(x, y, r, color_r, color_g, color_b)

n_flowers(40)

#triangle(20,-100,40)

# TODO: Utvidelse interaksjon på klikk

mainloop() # Settes på slutten av programmet for å hindre at tegningen lukkes