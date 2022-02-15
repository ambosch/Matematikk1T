# Hentet fra boken Matematikk 1T
from pylab import *

print("Programmet skal løse andregradslikningen")
print("ax^2 + bx + c = 0 ved hjelp av abc-formelen.")
print("Skriv inn verdiene for a, b og c.")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b**2 - 4*a*c

if d == 0:
    x = -b/(2*a) # Her brukes enkel x i stedet for x1, eller x0.
    print("Løsningen på andregradslikningen er: ")
    print("x =", x)
elif d < 0:
    print("Andregradslikningen har ingen løsning.")
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    x1 = round(x1, 2)
    x2 = round(x2, 2)
    print("Løsningen på andregradslikningen er: ")
    print("x1 =", x1, "og x2 =", x2)

"""
Dette løsningsforslaget ligger på Aunivers sine sider

Til forskjell fra Sinus sitt program tar det ikke hensyn til input der a = 0. Dette kunne vært nok en utvidelse å gi til elevene
"""