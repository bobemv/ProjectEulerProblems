__author__ = 'Roberto Moreno'

import math

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

def rotacionesNumero(numero):

    lista = []

    n = numero
    for i in range(len(str(numero))):
        lista.append(n)
        firstDigit = n%10
        n //= 10
        n += (10**(len(str(numero))-1)*firstDigit)

    return lista


"Solucion: 55. Se puede mejorar mucho (evitar repetidos y evitar aquellos numeros con una cifra par)"
top = 100000
contador = 1; "Contamos ya el 2"

for i in range(3, top, 2):
    flag = True

    for rot in rotacionesNumero(i):
        if not esPrimo(rot):
            flag = False
            break


    if flag:
        contador += 1


print contador