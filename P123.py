__author__ = 'Roberto Moreno'

import math
import time

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


contador = 2; "Se encontrara con el 5 primero y sumara"
numero = 6
flag = False
top = 10**10

t = time.clock()

while not flag:
    "El remainder es 2 en el n par primo"
    if esPrimo(numero - 1):
        contador += 1
        "???"
        if contador % 2:
            remainder = (((numero - 2)**contador) + ((numero)**contador)) % ((numero - 1)**2)
            print contador, numero - 1, remainder
            if remainder > top:
                flag = True
                numero -= 1
                break

    if esPrimo(numero + 1):
        contador += 1
        if contador % 2:
            remainder = (((numero)**contador) + ((numero + 2)**contador)) % ((numero + 1)**2)
            print contador, numero+1, remainder
            if remainder > top:
                flag = True
                numero += 1
                break

    numero += 6

print contador, numero, remainder, time.clock() - t
"Solucion: 21035 237737 10001595590 88.364352"