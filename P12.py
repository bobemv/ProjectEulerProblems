__author__ = 'roberto'

import math
def numFactoresNumero(numero):
    triangulo=0
    contador = 0
    i = 0
    while contador <= numero:
        contador = 0
        i+=1
        triangulo+=i
        for j in range(1, int(math.floor(math.sqrt(triangulo)))+1):

            if triangulo%j == 0:
                a = j
                b = triangulo/j
                if a > b:
                    break
                elif a==b:
                    contador+=1
                else:
                    contador+=2

    return triangulo

print numFactoresNumero(500)

