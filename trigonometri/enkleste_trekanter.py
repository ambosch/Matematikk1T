# Programmet tegner 1 trekant
from turtle import *

def trekant():
    for n in range(3):
        forward(100)
        left(180 - 60)

trekant()

mainloop()

