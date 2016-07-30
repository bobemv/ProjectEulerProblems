__author__ = 'Roberto Moreno'

import time

def funcionv5():
    flag = False
    lista = []
    lista.append(1)
    numero = 0
    while not flag:
        numero += 1

        suma = 0

        "Positivos"
        j = 1
        x = numero - (j*(3*j-1)//2)
        while x >= 0:
            suma += int((-1)**(j-1))*lista[x]
            j += 1
            x = numero - j*(3*j-1)//2


        "Negativos"
        j = -1
        x = numero - j*(3*j-1)//2
        while x >= 0:
            suma += int((-1)**(j-1))*lista[x]
            j -= 1
            x = numero - j*(3*j-1)//2

        lista.append(suma)

        if numero == 100:
            return numero, suma-1



a = time.clock()

print funcionv5(), time.clock()-a
