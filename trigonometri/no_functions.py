'''
Programmet tegner trekanter uten å bruke funksjoner.
'''

from turtle import *
import math

speed(3)

# Likesidet trekant
for n in range(3):
    forward(100)
    left(120) # Indre 60 grader

clear()
goto(0,0)

# 30-60-90 rettvinklet trekant
forward(300)
left(90) # 90-grader
forward(300*math.sqrt(3))
left(180-30) # Supplementvinkel
forward(600)


mainloop()