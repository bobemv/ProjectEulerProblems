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

def sumaPrimos(cota, funcion=esFactor):
    contador = 1;
    i = 2;
    suma = 0

    for i in range(2, cota):
        print i
        if funcion(i):
            suma += i
        i+=1;
    return suma

def sumaPrimosv2(cota, funcion=esFactor):
    "Segun el autor de Project Euler"
    suma = 5
    n = 5
    while n <= cota:
        if funcion(n):
            suma += n
        n+=2
        if n<= cota and funcion(n):
            suma += n
        n+=4

    return suma

def sumaPrimosAutor(cota):
    "Usando memoria principal (array booleans)"
    "No funciona aun"
    sieveBound = (cota-1)//2
    sieve = [False for i in range(sieveBound)]
    crossLimit = int((math.floor(math.sqrt(cota))-1)//2)

    for i in range(1, crossLimit+1):
        if not sieve[i]:
            for j in range((2*i*(i+1)), sieveBound):
                sieve[j]=True


    sum = 2
    for i in range(1, sieveBound):
        if not sieve[i]:
            sum+=2*i+1

    return sum

print sumaPrimosAutor(2000000)
