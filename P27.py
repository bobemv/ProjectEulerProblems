__author__ = 'Roberto Moreno'
import math

def esPrimo(numero):
    flag = True

    for i in range(2, int(math.floor(math.sqrt(numero)))+1):
        if numero%i == 0:
            flag = False
            break
        i+=1;

    return flag

contador = 0
a, b = 0, 0

for i in range(-999, 999):
    for j in range(-999, 999):
        n = 0
        numero = n**2+i*n+j
        if numero < 0:
            continue
        while esPrimo(numero):
            n+=1
            numero = n**2+i*n+j
            if (numero<0):
                break
        if (n>contador):
            a = i
            b = j
            contador = n

print a, b, contador