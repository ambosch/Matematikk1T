import matplotlib.pyplot as plt

def f(x):
    return 5000*1.25**x

xstart = 0
xslutt = 8
xsteg = 0.01
delta_x = 0.01

x = xstart
xverdier = []   # Bruker lister i stedet for array datatype (trenger derfor ikke numpy)
yverdier = []
derivertverdier = []

while x <= xslutt: # Kan ikke direkte lage en liste slik som med array, og looper derfor gjennom i stedet
    xverdier.append(x)
    y=f(x)
    yverdier.append(y)
    derivert = (f(x+delta_x)-f(x))/delta_x
    derivertverdier.append(derivert)
    x += xsteg

plt.plot(xverdier,yverdier,label="f(x)")
plt.plot(xverdier, derivertverdier, label="f'(x)")
plt.legend()
plt.show()