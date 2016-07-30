__author__ = 'Roberto Moreno'

import math

def esFactor(numero):
    flag = True
    for i in range(2, int(math.floor(math.sqrt(numero)))+1):
        if numero%i == 0:
            flag = False
            break
        i+=1;

    return flag

def esFactorv2(numero):
    "Metodo de la Criba de Erastotenes"
    "Todo primo mayor que 3 puede ser escrito como 6k+/-1"

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

def obtenerPrimo(posicion, funcion=esFactor):
    contador = 1;
    i = 2;

    while contador < posicion:
        i+=1
        if funcion(i):
            contador+=1

    return i

print obtenerPrimo(10001, funcion=esFactorv2)



