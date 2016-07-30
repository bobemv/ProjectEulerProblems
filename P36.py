__author__ = 'Roberto Moreno'

import math
import decimal
import time

def esPalindromo(numero):
    invertido = 0;
    derecho = numero;
    while derecho >= 1:
        invertido *= 10
        invertido += derecho % 10
        derecho //= 10

    if invertido == numero:
        return True
    return False

def sumaPalindromosDecYBin(max=1000000):
    contador = 0
    maximo = bin(max)
    maximo = maximo[2:]; "Tenemos el tope max como binario"

    suma = 1 + 3; "Primeros numeros palindromos en ambas bases"
    binario = ['1', '0', '1']
    numBinario = str(101)

    while int(maximo, 2) > int(numBinario, 2):
        comb = int(math.ceil(decimal.Decimal((len(binario)-2))/2))
        combinaciones = int(2**math.ceil(decimal.Decimal((len(binario)-2))/2))

        "Numero de palindromos de n digitos en binario"
        for i in range(combinaciones):
            num = bin(i)
            num = num[2:]
            num = num.zfill(comb); "Que basto tu, se llena con leading zeros"
            reverse = list(num)
            reverse.reverse()

            if len(binario)%2 == 0:
                mutable = ['1'] + list(num) + reverse + ['1']
            else:
                mutable = ['1'] + list(num) + reverse[1:] + ['1']

            n = ''.join(mutable)
            numero = int(n, 2)

            contador += 1
            if numero < max:
                if esPalindromo(numero):
                    suma += numero


        binario.insert(1, '0')
        numBinario = ''.join(binario)


    return suma, contador

def sumaPalindromosBruto(max=1000000):

    i = 1
    suma = 0

    while i < max:

        if esPalindromo(i):
            binario = bin(i)
            binario = binario[2:]
            binary = int(binario)
            if esPalindromo(binary):
                suma += i

        i += 2

    return suma

c = time.clock()
print sumaPalindromosDecYBin(1000000000), time.clock()-c
