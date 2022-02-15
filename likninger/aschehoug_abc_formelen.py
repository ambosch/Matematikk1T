# Hentet fra Matematikk 1T s. 123
from pylab import *
print("Programmet skal løse andregradslikningen")
print("ax^2 + bx + c = 0 ved hjelp av abc-formelen.")
print("Skriv inn verdiene for a, b, og c.")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b**2 - 4*a*c

x1 = (-b + sqrt(d))/(2*a)
x2 = (-b - sqrt(d))/(2*a)

print("Løsningen på andregradslikningen er")
print("x1 =",x1,"og x2 =",x2)

'''
Programmet er bare et skjelett når elevene får det.
Først tester de at det fungerer når to løsninger finnes.
De må selv implementere tilfellene
1. Det er én løsning --> Samme løsning skrives ut to ganger nå
2. Det er ingen løsning --> I dette tilfellet får man en feilmelding om "invalid value encountered in sqrt"
3. Skrive ut svaret med to desimaler --> Nå er det maksantall 15 som skrives ut

Refleksjoner:
Elevene må selv implementere algoritmen, og dette kan gjøres på mer eller mindre elegante måter
Elevene kan faktisk bruke programmet som det står nå, for om det krasjer så må det jo være ingen løsninger
Fordelen ved å regne andregradslikninger for hånd er at man ikke får desimaltall, men bruker rottegn og brøker og får eksakte løsninger
'''
