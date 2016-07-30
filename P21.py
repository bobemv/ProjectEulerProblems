import math

__author__ = 'Roberto Moreno'

def sumaFactoresNumero(numero):
    contador = 0
    suma = 0
    for j in range(1, int(math.floor(math.sqrt(numero)))+1):

        if numero%j == 0:
            a = j
            b = numero/j
            if a > b:
                break
            elif a==b:
                contador+=1
            else:
                contador+=2

            if b == numero:
                b = 0
            suma += a+b

    return suma

def sumaNumerosAmigablesv2(maximo):
    i = 1
    j = 1
    inicio = 1
    suma = 0

    for i in range(1, maximo):
        suma1 = sumaFactoresNumero(i)
        if(suma1%2 == i%2):
            if suma1%2 == 1 and suma1%3 != 0:
                continue
            suma2 = sumaFactoresNumero(suma1)
            if (suma2 == i):
                if(suma1 == suma2):
                    continue
                suma += suma1 + suma2
                print suma1, suma2, " -- Suma:", suma

    return suma/2

print sumaNumerosAmigablesv2(10000)