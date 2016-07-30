__author__ = 'Roberto Moreno'
import math

def encontrarTripletePitagorico(suma=1000):
    for a in range(1, (suma//3)):
        for b in range(a+1, (suma//2)-a//2):
            c = suma - a - b
            print a, b , c
            if (a**2)+(b**2) == c**2 :
                return a*b*c, a, b, c

print encontrarTripletePitagorico()
