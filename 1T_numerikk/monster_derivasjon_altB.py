import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 5000 * 1.25 ** x


delta_x = 0.01
xmin = 0
xmaks = 8
antall_punkter = 1000
a = np.linspace(xmin, xmaks, antall_punkter)    # Returnerer en Array, som er noe litt annet enn liste
y = f(a)                                        # Også en array, da den tar inn en array
yderivert = (f(a + delta_x) - f(a)) / delta_x   # Også en array

plt.plot(a, y, label="f(x)")
plt.plot(a, yderivert, label="f'(x)")
plt.legend()
plt.show()


