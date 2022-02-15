# Programmet plotter funksjonen f(x) og den deriverte med tre ulike implementasjoner av numerisk derivasjon

import numpy as np # brukes ikke i denne implementasjonen
import pylab as plb

# Les mer om numerisk derivasjon her
# https://en.wikipedia.org/wiki/Numerical_differentiation

def funksjon(x): # Funksjonen må være kontinuerlig på det valgte intervallet i linspace
    return 4*x**4 + 3*x**3 +2

# Valg av verdi for delta_x er av betydning for resultatet
delta_x = 0.1

# Valg av derivasjonsmetode er av betydning for resultatet
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


