# Brukerinput
a = float(input("Verdien til a ")) # Float mer hensiktsmessig enn int
b = float(input("Verdien til b "))
c = float(input("Verdien til c "))


# Programfunksjoner
def f():
    return f"f(x)={a}x**2 + {b}x + {c}"  # Knotete format for riktig utskrift med verdier og strenger


def derivert():
    return f"f'(x)={2 * a}x + {b}"


print(f())
print(derivert())

x = float(input("x-verdi "))


def f(x): # Samme funksjonsnavn er lov å repetere når man har ulikt antall parametre
    return a * x ** 2 + b * x + c  # Rar syntaks for potenser og tvunget multiplikasjonstegn


def derivert(x):
    return 2 * a * x + b


print(f"f({x})=", end="")  # Endelsesparameter for å overkjøre ny lije
print(f(x))
print(f"f'({x})=", end="")  # x brukes både som streng og tallverdi
print(derivert(x))
