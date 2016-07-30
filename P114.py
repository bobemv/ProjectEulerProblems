__author__ = 'Roberto Moreno'

import time

def funcion114(numero):
    "Formula -> p(n) = p(n-1) + (n-2) + 1/2((n-6)*(n-5)/2 + (n-6)*(n-5)(2n-11)/6)"
    if numero == 6:
        return 11
    elif numero == 1 or numero == 2 or numero == 3:
        return 2
    elif numero == 4:
        return 4
    elif numero == 5:
        return 7

    nuevaParte = numero - 2
    nuevaParte += (((numero-6)*(numero-5))/2 + ((numero-6)*(numero-5)*(2*numero-11))/6)/2

    return nuevaParte + funcion114(numero-1)


def funcion114v2(numero, inicio=3):

    tabla = []
    tabla.append(0)
    tabla.append(0)
    tabla.append(2)
    tabla.append(4)
    tabla.append(7)
    tabla.append(11)

    for i in range(7, numero):
        tabla.append(recursion114(i, tabla, inicio))

    return recursion114(numero, tabla, inicio)



def recursion114(numero, tabla, inicio=3):

    suma = 0
    for i in range(inicio, numero - (inicio)):
        suma += tabla[i-1]

    suma += (inicio + 1)

    return tabla[numero-2] + suma


t = time.clock()
print funcion114v2(30), time.clock()-t

