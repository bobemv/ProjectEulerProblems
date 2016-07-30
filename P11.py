__author__ = 'Roberto Moreno'

def maximoMulMatriz(matriz, adyacentes=4):
    "Suponiendo matriz cuadrada"
    longitud = matriz.__len__()
    maximo = 0

    "Chequear horizontales"
    for i in range(longitud-adyacentes):

        for j in range(longitud-adyacentes):
            mul = 1
            for z in range(adyacentes):
                mul *= matriz[i][j+z]
            if mul>maximo:
                maximo = mul

    "Chequear verticales"
    for i in range(longitud-adyacentes):

        for j in range(longitud-adyacentes):
            mul = 1
            for z in range(adyacentes):
                mul *= matriz[i+z][j]
            if mul>maximo:
                maximo = mul


    "Chequear diagonales"
    for i in range(longitud-adyacentes):
        for j in range(adyacentes-1, longitud):
            mul = 1
            for z in range(adyacentes):
                mul *= matriz[i+z][j-z]
            if mul>maximo:
                maximo = mul

    for i in range(longitud-adyacentes):
        for j in range(longitud-adyacentes+1):
            mul = 1
            for z in range(adyacentes):
                mul *= matriz[i+z][j+z]
            if mul>maximo:
                maximo = mul

    return maximo


f = open('P11Data.txt', 'r')

l = [ map(int,line.split(' ')) for line in f if line.strip() != "" ]


print maximoMulMatriz(l)