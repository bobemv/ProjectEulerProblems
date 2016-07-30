__author__ = 'Roberto Moreno'

import time
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def funcion126():

    x = 1
    y = 1
    z = 1
    limiteCoord = 5000
    limiteX = 50
    limiteY = 100
    limiteZ = 5000
    limitezaux = 5000
    limiteCapas = 70
    contador = 0
    mapas = dict()

    for x in range(1, limiteX+1):
        for y in range(x, limiteY+1):
            for z in range(y, limiteZ+1):
                print x, y, z
                "Calculamos la primera capa y la anadimos"
                primeraCapa = 2 * ((x*y)+(x*z)+(y*z))

                if not primeraCapa in mapas:
                    mapas[primeraCapa] = 1
                else:
                    mapas[primeraCapa] += 1

                "Calculamos la constante 'escalera' que sera usada en todas las capas"
                escalera = 4 * (x+y+z)
                contadorEscalera = 1

                "Calculamos las capas segun la formula: capaActual = primeraCapa + (n-1)*escalera + 8*(n-2) donde n es el numero de la capa"
                sumatorioOcho = 0
                contadorSumatorioOcho = 0

                for aux in range(limiteCapas):

                    nuevaCapa = primeraCapa + (escalera*contadorEscalera) + sumatorioOcho * 8
                    if not nuevaCapa in mapas:
                        mapas[nuevaCapa] = 1
                    else:
                        mapas[nuevaCapa] += 1

                    contadorEscalera += 1
                    contadorSumatorioOcho += 1
                    sumatorioOcho += contadorSumatorioOcho

            limiteZ -= 10
        limiteZaux =- 100
        limiteZ = limitezaux
    return mapas


t = time.clock()
mapas = funcion126()
print time.clock() - t

minim = 999999
for key, value in mapas.items():
    if value == 1000 and key < minim:
        minim = key

print minim

