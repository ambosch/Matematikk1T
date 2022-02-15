def f(x):
    return 5000 * 1.25**x

def fderivert(a):
    delta_x = .01
    return (f(a+delta_x)-f(a))/delta_x

a=0 #startverdi
trinn = 0.01

while fderivert(a) < 3000:
    a = a+trinn

print(f"Løsning er x = {a:.3f}")