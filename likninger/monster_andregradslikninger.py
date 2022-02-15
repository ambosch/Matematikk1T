# Mønster 1T s. 91

import math

a = 1
b = 2
c = 3

D = b**2 - 4*a*c # Stor D for diskriminanten

if D < 0:
    print("Likningen har ingen løsning.")
elif D == 0:
    print(f"Likningen har løsning x = {-b/(2*a):.3f}") # Her hadde de i boka glemt å skrive f foran setninga, med andre ord enda en kodefeil knyttet til formattering
else:
    x_1 = (-b + math.sqrt(D))/(2*a)
    x_2 = (-b - math.sqrt(D))/(2*a)
    print(f"Løsningen av likningen er x = {x_1: .3f} eller x = {x_2: .3f}.")

'''
I likhet med Aschehoug sin bok tar ikke programmet høyde for a = 0
Programmet gjenbruker boka strengformattering but why
Kanskje et bra førstesteg å utelate brukerinput her? Programmet er ikke helt gjenbrukbart med en gang, men det gjør ikke så mye da det er til for elevens læring
'''
