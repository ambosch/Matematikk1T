import turtle
import math
import random

'''
Trigonometriprogram
Benytter både arealsetningen og cosinussetningen
Kan kanskje modifiseres til å løses med sinussetningen

Hvordan det virker:
Tegningen bytter farge når det samlede arealet overstiger verdien til variabelen maksareal som sendes inn i funksjonen tegn(maksareal) i linje 117
'''
colors = ["red","blue", "green","pink", "yellow","purple", "magenta", "lightseagreen"] # Innebygde CSS-farger: https://www.w3schools.com/cssref/css_colors.asp
colors2 = ["#D8F3DC","#B7E4C7","#95D5B2","#74C69D","#52B788","#40916C","#2D6A4F","#1B4332"] # Fargepalett: https://coolors.co/palette/d8f3dc-b7e4c7-95d5b2-74c69d-52b788-40916c-2d6a4f-1b4332-081c15

# Uendelig løkke startes når programmet startes
running = True
def tegn(maksareal):
    areal = 0 # Startbetingelse i while-løkka
    while running==True:
        if areal < maksareal:
            AB = random.randint(1, 100)
            AC = random.randint(1, 100)
            theta = random.randint(1, 179)  # 0 og 180 grader gir ingen trekant, over 360 grader blir tull

            trekantareal = arealsetningen(AB, AC, theta)

            # tegner
            x = random.randint(-50,50) # Området som tegnes i kan gjerne utvides
            y = random.randint(-50,50)
            h = random.randint(0,360) # Hodets retning
            turtle.penup()
            turtle.goto(x,y)
            turtle.setheading(h)

            turtle.pendown()
            trekant(AB, AC, theta)
            areal += trekantareal # Når vi når maksareal byttes fargen
        else:
            turtle.penup()
            index = random.randint(0, len(colors2) - 1) # Velger farge fra lista tilfeldig
            turtle.color(colors2[index])
            turtle.fillcolor(colors2[index])
            areal = 0 # Resetter fargens samlede areal



def arealsetningen(AB,AC,theta): # vinkelen i grader tas inn
    return (1/2)*AB*AC*math.sin(math.radians(theta)) # Finner arealet av trekanten ofte, men her skjer det noe rart med vinklene

def cosinussetningen_finnside(AB, AC, theta): # vinkelen i grader tas inn
    return math.sqrt(AB**2 + AC**2 - 2*(AB*AC)*math.cos(math.radians(theta))) # Finner siden BC, ikke BC**2

def cosinussetningen_finnvinkel(AB,AC,BC):
    cos_c = (AB**2-AC**2-BC**2)/(-2*AC*BC)
    C = math.degrees(math.acos(cos_c))
    return C

def trekant(AB,AC,theta): # Ofte riktig, men noen ganger blir de kryss. Sikkert noe med spiss vinkel å gjøre
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(AB)
    turtle.left(180 - theta)
    turtle.forward(AC)
    BC = cosinussetningen_finnside(AB, AC, theta) # Finner lengden av sida
    C = cosinussetningen_finnvinkel(AB, AC, BC)
    turtle.left(180-C)
    #turtle.goto(x,y) # I stedet for å finne vinkel C og side BC, kan vi returnere til startpunktet for trekanten
    turtle.forward(BC)
    turtle.end_fill()

# Funksjoner for programinteraksjon
def quit():
    global running # Nøkkelordet global må brukes for å aksessere den globale variabelen
    running = False

def start():
    global running
    running = True
    tegn(maksareal) # Må kalle funksjonen på nytt fordi while-løkka har stoppa

def clear():
    turtle.clear()

def dark():
    turtle.bgcolor("#191919")

def light():
    turtle.bgcolor("#FCFFFC")


def original():
    turtle.bgcolor(bg_start)

# Oppsett del 1: Konfigurasjon av programmet
screen = turtle.Screen()
screen.setup(600,600) # Setter vindustørrelse (inkludert topp, og bunnmarg)
turtle.listen() # For at interaksjon med tastaturet skal fanges opp av programmet
turtle.onkeypress(quit, "q") # Kaller funksjonen quit når q trykkes på tastaturet
turtle.onkeypress(start, "s") # Restarter programmet med fargen vi slutta på (areal for fargen resettes, så ikke helt perfekt her)
turtle.onkeypress(dark,"d") # Dark mode
turtle.onkeypress(light, "l") # Light mode
turtle.onkeypress(original, "o") # Original bakgrunnsfarge
turtle.onkeypress(clear,"c") # Tøm skjermen

# Oppsett del 2: Setter hastighet, farger og maksareal
turtle.shape("turtle")
bg_start = "#081C15" # BG også fra coolors fargepalett
turtle.bgcolor(bg_start) # Bakgrunnsfarge for kunstverket
turtle.speed(0) # Raskeste fart 0
startcolor = random.randint(0,len(colors2))
turtle.color(colors2[startcolor]) # Første farge
turtle.fillcolor(colors2[startcolor])
maksareal = 10000

# Starter programmet
tegn(maksareal) # Veldig store tall på maksareal på grunn av pikslene, kan endres til å bruke cm
turtle.mainloop() # For ikke å skape programkrasj ved bruk av turtle
