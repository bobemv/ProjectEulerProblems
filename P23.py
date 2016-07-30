__author__ = 'Roberto Moreno'
import math

def sumaFactoresNumero(numero):
    contador = 0
    suma = 0
    for j in range(1, int(math.floor(math.sqrt(numero)))+1):

        if numero%j == 0:
            a = j
            b = numero/j
            if a > b:
                break
            elif a==b:
                contador+=1
                suma += a
            else:
                contador+=2
                suma += a + b

    return suma-numero

def sumaNumerosCompuestosAmigables():
    lista = [i for i in range(1, 28124) if sumaFactoresNumero(i)>i]
    setAmigables = set()
    suma = 0
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if not lista[i]+lista[j]>28123:
                setAmigables.add(lista[i]+lista[j])

    print setAmigables
    for i in range(1, 28124):
        suma += i
    for i in setAmigables:
        suma -= i
    return suma


print sumaNumerosCompuestosAmigables()
