__author__ = 'roberto'

def sumaCifras(numero):

    suma = 0
    lista = [int(i) for i in str(numero)]

    for i in range(lista.__len__()):
        suma += lista[i]

    return suma

print sumaCifras(2**1000)