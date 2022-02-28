'''
Oppgave 1:
Ta inn alle sidelengdene fra brukeren. Tegn trekanten.
Finnes det trekanter for alle mulige kombinasjoner av sider? Nei, 600, 25, 99 feks gir en cosinusverdi på 11, som er mye mer enn 1
Finnes det ulike trekanter for samme sider? Nei, de må være kongruente (?).
Cosinussetningen
'''
import math
import turtle

s1 = float(input("Side 1"))
s2 = float(input("Side 2"))
s3 = float(input("Side 3"))


def vinkel(mot, v, h):
    cos_v = (mot**2 - v**2-h**2)/(-2*(v*h))
    print(cos_v) # Fordi her kom feilmeldingen
    v = math.degrees(math.acos(cos_v))
    return v

turtle.forward(s1)
turtle.left(180-vinkel(s3,s1,s2))
turtle.forward(s2)
turtle.left(180-vinkel(s1, s2, s3))
turtle.forward(s3)

turtle.mainloop()