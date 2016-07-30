__author__ = 'Roberto Moreno'

import math
from fractions import Fraction

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def factoresNumero(numero):
    lista = []
    n = numero
    i = 2
    while n%i == 0:
        n /= i
        lista.append(i)

    i += 1
    while n > 1:
        if i > int(math.floor(math.sqrt(n))):
            lista.append(n)
            break
        while n%i == 0:
            n /= i
            lista.append(i)
        i += 2

    return lista

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

def funcion530(k):
    suma = 1
    lista = []
    lista.append(1)
    for i in range(2, k+1):
        print i
        if esPrimo(i):
            lista.append(2)
            suma += 2
        else:
            factores = factoresNumero(i)
            factor = factores.pop(0)
            numerolista = reduce(lambda x,y: x*y, factores)
            "Sumamos tantas veces como aparezca el nuevo numero"
            aparicionesfactor = factores.count(factor) + 1
            if aparicionesfactor > 1:
                numero = factor*2
            else:
                numero = 2

            "Comprobamos combinaciones con otros factores unicos"
            factoresunicos = set(factores)
            for j in factoresunicos:
                apariciones = factores.count(j)
                if apariciones >= aparicionesfactor and aparicionesfactor % 2 == 0:
                    numero += ((factor**(apariciones//2))*(j**(apariciones//2))) * 2
            numero += lista[numerolista-1]

            if is_square(i):
                numero -= math.sqrt(i)

            lista.append(numero)
            suma += numero



    return suma

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def auxiliar(k):
    numero = 2
    for i in range(2, k):
        if(k%i == 0):
            numero += gcd(i, k//i)

    return numero

def auxiliar2(n):
    for i in range(2, n+1):
        print factoresNumero(i), auxiliar(i)

print auxiliar2(1000)


