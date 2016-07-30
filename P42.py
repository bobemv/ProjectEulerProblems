__author__ = 'Roberto Moreno'
import math

f = open("P42Data.txt", "r")

lista = [map(str,line.split('","')) for line in f if line.strip() != "" ]

lista2 = lista[0]

lista2[0] = lista2[0][1:]

print lista2

contador = 0

for palabra in lista2:
    suma = 0
    for i in palabra:
        suma += ord(i)-64

    suma *= 2
    raiz = math.sqrt(suma)

    suelo = math.floor(raiz)
    techo = math.ceil(raiz)
    if suma == suelo*techo and suelo != techo:
        print palabra, suma//2
        contador += 1


print "Numero palabras: ", contador