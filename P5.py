__author__ = 'Roberto Moreno'
import math

def esFactor(numero):
    flag = True
    for i in range(2, int(math.floor(math.sqrt(numero)))+1):
        if numero%i == 0:
            flag = False
            break
        i+=1;

    return flag


def minimoMultiploRango(maximo):
    mul = 1;
    proxy = mul;
    for i in range(1, maximo+1):
        for j in range(2, i+1):
            if esFactor(j):
                iproxy = i
                while iproxy%j == 0:
                    if proxy%j == 0:
                        proxy /= j
                    else:
                        mul *= j
                        print j
                    iproxy/=j
        proxy = mul;

    return mul

print minimoMultiploRango(100)
print esFactor(2)