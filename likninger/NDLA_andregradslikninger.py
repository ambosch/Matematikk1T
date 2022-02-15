# Hentet fra NDLA: https://ndla.no/nb/subject:1:8bfd0a97-d456-448d-8b5f-3bc49e445b37/topic:1:f638ea12-ddf0-4472-a0d5-3d498dc5275a/topic:4:1:165288/resource:b9eb8018-d0c6-41df-9728-f11b7fd9e42e

# Skriv til skjermen "Dette programmet løser andregradslikningen ax^2 + bx + c = 0.".
print("Dette programmet løser andregradslikningen ax^2 + bx + c = 0")

# Skriv til skjermen "Skriv inn konstanten a:".
print("Skriv inn konstanten a:")
#Ta imot tallet fra brukeren, konverter det til et ekte tall, og sett det lik variabelen a.
a = float(input())
# Skriv til skjermen "Skriv inn konstanten b:".
print("Skriv inn konstanten b:")
# Ta imot tallet fra brukeren, konverter det til et ekte tall, og sett det lik variabelen b.
b = float(input())
# Skriv til skjermen "Skriv inn konstanten c:".
print("Skriv inn konstanten c:")
# Ta imot tallet fra brukeren, konverter det til et ekte tall, og sett det lik variabelen c.
c = float(input())

# Regn ut x1 med formelen ovenfor, og sett resultatet lik variabelen x1.
import math #Dette måtte man finne ut av selv gitt oppgaveteksten
x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
# Regn ut x2 med formelen ovenfor, og sett resultatet lik variabelen x2.
x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)

# Skriv til skjermen "Løsningene er x1 = <x1> og x2 = <x2>.".
# I siste linje betyr "<x1>" innholdet av variabelen x1.
print("Løsningene er x1 = ",x1,"og x2 = ",x2) # Her må eleven finne ut av formatteringen selv


'''
Refleksjoner
Elevene må selv skrive implementasjonen av programmet basert på en detaljer pseudokode. Dette liker jeg.
Pseudokoden er lagt inn for hver linje i programmet.
Pseudokode og flytdiagrammer kan være en måte å finne sweet-spoten mellom instrumentalistisk avskriving og frykten for et tomt ark

Elevene må selv løse problemet med å importere for å få tak i funksjonen sqrt()
Elevene må selv finne ut hvordan de vil formattere utskriften av de to løsningene

Elevene skal deretter teste programmet for spesifikke andregradslikninger.
De må selv utvide programmet slik at det er tilpasset 1 løsning og ingen løsninger

Det er ikke nevnt noe om avrunding av svar eller om å ta hensyn til a=0.
'''