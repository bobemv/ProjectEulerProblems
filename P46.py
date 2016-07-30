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


flag = False

numero = 7
while not flag:
    numero += 2
    flag2 = False
    if not esPrimo(numero):
        for i in range (3, numero, 2):
            if esPrimo(i):
                x = numero - i
                x /= 2
                y = math.floor(math.sqrt(x))
                if y**2 == x:
                    print numero,"=", i, "+ 2*(", y, ")^2"
                    flag2 = True
                    break

        if not flag2:
            flag = True

print "No se puede escribir: ", numero