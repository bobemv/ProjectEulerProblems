__author__ = 'Roberto Moreno'

import math;
def numeroFibonacci(n):
    "0, 1, 1, 2, 3, 5, 8, 13, 21, 34"
    aureo = (1 + math.sqrt(5))/2;
    ret = (aureo**n-(1-aureo)**n)//math.sqrt(5)
    return ret

def tamanioNumero(numero):
    contador = 0
    while numero >= 1:
        numero/=10
        contador+=1
    return contador

i = 2
fibo1 = 1
fibo2 = 1
fibo = 2
while tamanioNumero(fibo) != 1000:
    i+=1
    fibo = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo
print i
