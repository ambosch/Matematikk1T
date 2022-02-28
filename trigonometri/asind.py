import math

# Tar inn et flyttall, returnerer den korresponderende vinkelen i grader
def asind(x):
    r = math.asin(x)
    d = math.degrees(r)
    return d

def acosd(x):
    r = math.acos(x)
    d = math.degrees(r)
    return d

print(asind(4**2/5**2)) # Returerer riktig verdi

print(acosd(0)) # Returnerer riktig verdi
