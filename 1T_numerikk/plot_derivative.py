import numpy as np # brukes visst ikke
import pylab as plb

# Les mer om numerisk derivasjon her
# https://en.wikipedia.org/wiki/Numerical_differentiation

def funksjon(x): # the function must be continuous on the interval
    return 4*x**4 + 3*x**3 +2

# Selection of delta x does matter
delta_x = 0.1

# Selection of differentiation definition does matter
def derivert_forover(x):
    return (funksjon(x + delta_x) - funksjon(x)) / delta_x


def derivert_bakover(x):
    return (funksjon(x) - funksjon(x - delta_x)) / delta_x


def derivert_symmetrisk(x):
    return (funksjon(x + delta_x) - funksjon(x - delta_x)) / (2 * delta_x)


y_f = []
y_b = []
y_s = []

x = plb.linspace(0.1,1.3,1001) # start, stop, number of values in between

plb.plot(x, funksjon(x), "b", label="f(x)")
plb.plot(x, derivert_forover(x), "r", label="f'(x)_f")
plb.plot(x, derivert_bakover(x), "g",label="f'(x)_b")
plb.plot(x, derivert_symmetrisk(x), "m",label="f'(x)_s")
plb.grid()
plb.legend()
plb.show()

'''
for i in range(1,101):
    y_f.append(derivert_forover(i))
    y_b.append(derivert_bakover(i))
    y_s.append(derivert_symmetrisk(i))


print(y_f)
print(y_b)
print(y_s)

'''
