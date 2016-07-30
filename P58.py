__author__ = 'Roberto Moreno'

import math
import decimal

def esPrimo(numero):
    if numero == 1:
        return False
    if numero<4:
        return True
    if numero%2 == 0:
        return False
    if numero<9:
        return True
    if numero%3 == 0:
        return False
    raiz = math.sqrt(numero)
    funcion = 5
    while funcion <= raiz:
        if numero%funcion == 0:
            return False
        if numero%(funcion+2) == 0:
            return False
        funcion+=6

    return True

primes = 8
diagonals = 13

squarelength = 7

while decimal.Decimal(primes) / decimal.Decimal(diagonals) >= 0.1:
    squarelength += 2
    num = squarelength**2
    diagonals += 1

    for i in range(3):
        num -= (squarelength - 1)
        if esPrimo(num):
            primes += 1
        diagonals += 1
    print squarelength, primes, diagonals

print squarelength, primes, diagonals
