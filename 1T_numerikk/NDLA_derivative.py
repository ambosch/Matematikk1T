def f(x):
    return x**4 +1

def derivert(x):
    return (f(x+ delta_x) - f(x))/delta_x

delta_x = 1

new = 1
old = 0

x = float(input("x-verdi "))


while abs(new - old)> 0.00001:
    delta_x *=0.1
    old = new
    new = derivert(x)

print("Den deriverte er", new, "når x = ",x, "og delta x = ",delta_x )
