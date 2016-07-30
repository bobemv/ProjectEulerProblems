__author__ = 'roberto'
import time
import math
import decimal
from sympy import binomial

import operator as op

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def comb(N,k): # from scipy.comb(), but MODIFIED!
    if (k > N) or (N < 0) or (k < 0):
        return 0L
    N,k = map(long,(N,k))
    top = N
    val = 1L
    while (top > (N-k)):
        val *= top
        top -= 1
    n = 1L
    while (n < k+1L):
        val /= n
        n += 1
    return val

"Vamos a calcular por pares"
def funcionv2():
    flag = False
    lista = []
    combinados = []

    "Se empieza en el 4"
    numero = 2
    acumulado = 0
    "Maneras de 0, 1, 2 y 3 monedas"
    lista.append(1)
    lista.append(1)
    lista.append(2)
    lista.append(3)

    acumulado = lista[1]

    while not flag:
        numero += 2

        sumapar = 2; "<-- Todo junto, o todo separado los montones de monedas. Hay dos por defecto"
        sumaimpar = 2
        mitadsup = (numero//2)+1

        sumapar += acumulado
        acumulado += lista[(numero//2)]
        sumaimpar += acumulado

        for i in range(2, mitadsup):
            k = (numero // i)-1

            "n es ahora el numero de packs sobrantes y cada uno se puede descomponer"

            n = lista[i]
            combinatorio = comb(n+k-1, k)
            resto = numero%i

            sumapar += combinatorio * lista[resto]

            if (numero+1)%i == 0:
                combinatorio = comb(n+k, k+1)
                sumaimpar += combinatorio
            else:
                sumaimpar += combinatorio * lista[resto+1]

        if sumapar % 1000000 == 0:
            flag = True
            return numero, sumapar

        if sumaimpar % 1000000 == 0:
            flag = True
            return numero+1, sumaimpar

        print numero, sumapar
        print numero+1, sumaimpar

        lista.append(sumapar)
        lista.append(sumaimpar)

    return numero


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
                suma += a
            else:
                contador+=2
                suma += a + b

    return suma-numero


"Vamos a hacer mierdas"
def funcionv3():
    flag = False
    lista = []
    combinados = []

    "Se empieza en el 4"
    numero = 3
    acumulado = 0
    "Maneras de 0, 1, 2 y 3 monedas"
    lista.append(1)
    lista.append(1)
    lista.append(2)
    lista.append(3)
    combinados.append(2)
    combinados.append(3)

    acumulado = lista[1]

    while not flag:
        numero += 1

        if numero % 2 == 1:
            acumulado += lista[(numero//2)]

        suma = 2; "<-- Todo junto, o todo separado los montones de monedas. Hay dos por defecto"
        mitadsup = (numero//2)+1

        suma += acumulado

        for i in range(2, mitadsup):

            resto = numero % i

            if resto == 0:
                if i-2 >= len(combinados):
                    combinados.append(comb(lista[i]+((numero//i)-1)-1, (numero//i)-1))
                else:
                    combinados.pop(i-2)
                    combinados.insert(i-2, comb(lista[i]+((numero//i)-1)-1, (numero//i)-1))

            suma += combinados[i-2] * lista[resto]

        if suma % 100000 == 0:
            flag = True
            return numero, suma

        print numero, suma


        lista.append(suma)

    return numero


"Fuck this fucking shit"
"Muchisimo mas rapido si no fuera por el uso de decimal"
def funcionv4():
    flag = False
    decimal.getcontext().prec = 10000
    lista = []
    lista.append(1)
    numero = 0
    while not flag:
        numero += 1

        suma = decimal.Decimal(0)

        "Positivos"
        j = 1
        x = numero - (j*(3*j-1)/2)
        while x >= 0:
            suma += decimal.Decimal(decimal.Decimal((-1)**(j-1))*lista[x])
            j += 1
            x = numero - long(j*(3*j-1)/2)


        "Negativos"
        j = -1
        x = numero - long(j*(3*j-1)/2)
        while x >= 0:
            suma += decimal.Decimal(decimal.Decimal((-1)**(j-1))*lista[x])
            j -= 1
            x = numero - long(j*(3*j-1)/2)

        lista.append(suma)
        print numero, suma

        if suma % 1000000 == 0:
            flag = True
            return numero, decimal.Decimal(suma)


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

        if suma % 1000000 == 0:
            return numero, suma



a = time.clock()

print funcionv5(), time.clock()-a


