'''
Oppgave:
Lag et program som tegner en likesidet trekant med sidelegden som sendes inn i funksjonen
Lag et program som tegner en likebeint trekant gitt grunnlinja og størrelsen til de to like vinklene
Endre programmet slik at du heller kjenner toppvinkelen og grunnlinja, Hvilke endringer måtte du gjøre? (ikke implementert i dette programmet)
'''

import turtle
import math

turtle.speed(8)
turtle.color("magenta")
turtle.bgcolor("darkgrey")
turtle.pensize(2)

def likesidet(sidelengde):
    for i in range(3):
        turtle.forward(sidelengde)
        turtle.right(180-60)

#likesidet(100)

# Bruker sinussetningen
def likebeint(s1,v1): # s1 er grunnlinja, v1=v2 er de like vinklene i trekanten
    s2 = None # De to like lange sidene har denne lengden
    v2 = None # Den siste vinkelen har denne størrelsen

    v2 = 180-2*v1

    sin_v2 = math.sin(math.radians(v2))
    sin_v1 = math.sin(math.radians(v1))

    s2 = (sin_v1/sin_v2)*s1

    turtle.forward(s1)
    turtle.left(180-v1)
    turtle.forward(s2)
    turtle.left(180-v2)
    turtle.forward(s2)
    turtle.left(180-v1) # Resetter vinkelen for head til å være der vi startet i trekanten


#likebeint(345,12) # Tester for ulike vinkler og sidelengder

# Bruker definisjonen av sinus for å løse samme problem som ovenfor
def likebeint2(s1,v1):
    halv_s1 = s1/2
    v2 = 180 - 2*v1
    halv_v2 = v2/2

    sin_halv_v2 = math.sin(math.radians(halv_v2))

    s2 = halv_s1/sin_halv_v2

    turtle.forward(s1)
    turtle.left(180-v1)
    turtle.forward(s2)
    turtle.left(180-v2)
    turtle.forward(s2)
    turtle.left(180-v1)


#likebeint2(300,25)

# Bruker funksjonen i et geometrisk mønster
for i in range(1,37):   # Nullindeksering gir en sidelengde 0
    likebeint(i*30,45)  # Økende sidelengde, men formlike trekanter
    turtle.left(10)     # Rotasjon rundt sentrum for hver trekant som tegnes



turtle.mainloop()       # Unngå at vinduet lukker seg