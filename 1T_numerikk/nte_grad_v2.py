print("Legg inn koeffisientene til polynomet i stigende rekkefølge")
print("Skriv stopp når du har skrevet inn alle koeffisientene")

koeffisienter = []  # Liste med koeffisientene
i = 0               # Starter med koeffisienten for x**0

running = True
while running == True:
    brukerinput = input(f"Koeffisient for ledd av grad {i} ")
    if brukerinput == "stopp":
        running = False # Stopper while-løkka
    try:
        brukerinput= eval(brukerinput) # eval skiller mellom float og int, kunne også brukt float her
        koeffisienter.append(brukerinput)
        i += 1
    except:
        pass # ugyldig input hoppes over, slik som bokstaver eller tegn


def f(liste,x): # Beregner funksjonsverdien til polynomet for en x-verdi
    verdi = 0
    for i in range(len(liste)):
        verdi += liste[i]*x**i
    return verdi


def f_derivert(liste,x): # Beregner verdien til den deriverte analytisk for en x-verdi
    verdi = 0
    if len(liste)>1:
        for i in range(1,len(liste)):
            verdi += i*liste[i]*x**(i-1)
    return verdi


def funksjonsuttrykk(liste):
    funksjon = ""
    funksjon += str(liste[0]) # Fordi x**0 = 1 forkortes
    for i in range(1,len(liste)): # forbedring: ikke x**1, men bare x
        funksjon = f"{liste[i]}x**{i} + " + funksjon # Printes ut med høyeste koeffisient først
    return funksjon

def derivertuttrykk(liste):
    derivert = ""
    if len(liste)==1:
        derivert += "0"
    # Første koeffisient deriveres uansett til 0
    if len(liste)>1:
        derivert += str(liste[1]) # Skal ikke ha x-ledd
    if len(liste)>2:
        for i in range(2,len(liste)):
            if liste[i] != 0: # fjerner ledd med 0-koeffisient
                derivert = f"{i*liste[i]}x**{i-1} + " + derivert
    return derivert

# Utskrift
print("f(x)=",funksjonsuttrykk(koeffisienter))
print("f'(x)=",derivertuttrykk(koeffisienter))
x = eval(input("Velg x-verdi "))
print(f"f({x})={f(koeffisienter,x)}")
print(f"f'({x})={f_derivert(koeffisienter,x)}")