__author__ = 'Roberto Moreno'
import math
import decimal
import itertools

def firstSort(lista):
    flag = False
    contador = 0
    while not flag:
        flag = True
        i = 0
        final = len(lista) - 2

        for j in range(0, final+1):
            if lista[j] > lista[j+1]:
                aux = lista[j+1]
                lista.pop(j+1)
                lista.insert(0, aux)
                contador += 1
                flag = False
                break

    return contador

suma = 0
n = 10
contador = 0
l = [i for i in range(1, n+1)]

for lista in itertools.permutations(l):
    suma += firstSort(list(lista))
    contador += 1
    print contador, suma

print "Esperado: ", (decimal.Decimal(suma)/decimal.Decimal(math.factorial(n)))