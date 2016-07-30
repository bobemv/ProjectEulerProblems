__author__ = 'Roberto Moreno'
import time

def funcion115(numero, inicio):

    tabla = []
    for i in range(1, inicio):
        tabla.append(0)

    suma = 2
    for i in range(2, inicio+3):
        tabla.append(suma)
        suma += i

    if numero < (2*inicio)+1:
        return tabla[numero-1]

    for i in range((2*inicio)+1, numero):
        tabla.append(recursion115(i, tabla, inicio))

    return recursion115(numero, tabla, inicio)



def recursion115(numero, tabla, inicio):

    suma = 0
    for i in range(inicio, numero - (inicio)):
        suma += (tabla[i-1] - 1)

    suma += (numero - inicio + 1)

    return tabla[numero-2] + suma


t = time.clock()

suma = 0
i = 0
while suma < 10**6:
    i += 1
    suma = funcion115(i, 50)

print i, suma, time.clock()-t