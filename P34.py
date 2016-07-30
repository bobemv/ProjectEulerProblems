__author__ = 'Roberto Moreno'

import math

def limite():
    suma = math.factorial(9) * 2
    n = 10

    while suma > n:
        suma += math.factorial(9)
        n *= 10

    return n


"Resultado: 40730"
def funcion():

    factoriales = [math.factorial(i) for i in range(10)]
    max = limite()
    suma = 0

    for i in range(10, max+1):

        digitos = [int(j) for j in str(i)]
        add = 0

        for j in range(len(digitos)):
            add += factoriales[digitos[j]]

        if i == add:
            suma += add
            print i, add


    return suma


def funcionv2(numero, factoriales, suma=0):


    additionv2 = 0
    for i in range(10):
        mutable = numero[:]
        mutable.append(str(i))

        numero = int(''.join(mutable))

        addition = 0

        for j in range(len(mutable)):
            addition += factoriales[int(mutable[j])]

        if addition > numero:
            break

        if addition == numero:
            print numero, addition
            additionv2 += addition
            break

        additionv2 += funcionv2(mutable, factoriales)
        mutable.pop()

    return additionv2




print funcion()

