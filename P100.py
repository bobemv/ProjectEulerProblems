__author__ = 'Roberto Moreno'

import math

def factoresNumero(numero):
    lista = []
    n = numero
    i = 2
    while n%i == 0:
        n /= i
        lista.append(i)

    i += 1
    while n > 1:
        if i > int(math.floor(math.sqrt(n))):
            lista.append(n)
            break
        while n%i == 0:
            n /= i
            lista.append(i)
        i += 2

    return lista

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def funcion():
    flag = False

    n = 15
    while not flag:
        n+=1
        print n
        raiz = 4+8*(n*n**2)

        numero = 2 + math.sqrt(raiz)

        if not numero%4 == 0:
            print "Not div 4"
            continue

        numero /= 4
        flag = True
    return n, numero

def funcionv2():
    flag = False
    n = 1000000
    numero = n
    bb = 0


    while not flag:
        prob = 0
        blue = math.floor(0.7071067811865476*n)
        prob = (blue*(blue-1))/(n*(n-1))

        while prob < 0.5:
            blue+=1
            prob = (blue*(blue-1))/(n*(n-1))

        if (n*(n-1)) % (blue*(blue-1)) == 0:
            print n, blue, prob
            flag2 = probabilidadDosBlueUnMedio(factoresNumero(n), factoresNumero(n-1), factoresNumero(blue), factoresNumero(blue-1))

            if flag2:
                numero = n
                bb = blue
                flag = True

        n+=1

    return numero, bb

def probabilidadDosBlueUnMedio(nactual, nanterior, blueactual, blueanterior):
    n = nactual
    n.extend(nanterior)

    blue = blueactual
    blue.extend(blueanterior)

    n.sort()
    blue.sort()

    flag = False

    if len(n) == len(blue)+1:
        flag = True
        for i in range(0, len(blue)):
            if not n[i+1] == blue[i]:
                flag = False
                break

    return flag

def funcionv3():
    flag = False

    n = 10**6
    while not flag:
        n+=1
        print n
        c = ((n**2)-n)/2

        blue = math.floor(0.7071067811865476*n)
        blue+=1

        if blue**2 - blue == ((n**2) - n)/2:
            numero = n
            bb = blue
            flag = True

    return numero, bb

def funcionv4():
    flag = False
    n = 100000
    numero = n
    bb = 0


    while not flag:
        prob = 0
        blue = math.ceil(0.7071067811865476*n)
        prob = (blue*(blue-1))/(n*(n-1))

        if (n*(n-1)) % (blue*(blue-1)) == 0:
            print n, blue, prob
            flag2 = probabilidadDosBlueUnMedio(factoresNumero(n), factoresNumero(n-1), factoresNumero(blue), factoresNumero(blue-1))

            if flag2:
                numero = n
                bb = blue
                flag = True

        n+=1

    return numero, bb

def funcionv5(numero):
    flag = False
    suma = 0
    i = numero
    suma = i*(i+1)/2
    while not flag:
        i+=1
        suma += i + (i+1) + (i+2)
        print i
        raiz = math.sqrt(suma)
        floor = math.floor(raiz)
        ceil = math.ceil(raiz)
        if floor*ceil == suma and floor != ceil:
            print "n = ", i+1, "blue = ", math.ceil(raiz)
            flag = True

        i += 3
        suma += i
        print i
        raiz = math.sqrt(suma)
        floor = math.floor(raiz)
        ceil = math.ceil(raiz)
        if floor*ceil == suma and floor != ceil:
            print "n = ", i+1, "blue = ", math.ceil(raiz)
            flag = True


print funcionv5(10**12)