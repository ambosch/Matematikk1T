# Hentet fra Sinus 1T eksempel s.115
from math import sqrt

print("Vi skal løse andregradslikningen ax^2+bx+c=0") # Forteller brukeren hv
svar = input("a = ")
a = float(svar)

if a == 0:
    print("Med a = 0 blir det ikke en andregradslikning") # Håndtering av ekstremtilfeller er høy måloppnåelse
else:
    svar = input("b = ")  # Overskriver variablen for svar hver gang, tydeliggjør at vi må parse string til int
    b = float(svar)
    svar = input("c = ")
    c = float(svar)
    d = b ** 2 - 4 * a * c  # Determinanten

    if d < 0:
        print("Ingen løsning")
    elif d == 0:
        x1 = -b / (2 * a)
        print("Én løsning x =", round(x1, 2))  # Unngår f-string literals
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("To løsninger x =", round(x1, 2), "og x =", round(x2, 2))


"""
I kapittelet skal elevene gjenbruke programmet for å løse spesifikke instanser av andregradslinkninger i oppgavene
Oppgave 3.168 på side 343 er spennende fordi den viser et flytdiagram over programflyten
Flytdiagram kan være et hensiktsmessig verktøy å bruke
Utvidelse: Løse tredjegradslikninger
"""
