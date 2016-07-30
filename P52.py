__author__ = 'Roberto Moreno'

def esPermutacionNumero(numero, permutacion):
    if len(str(permutacion)) != len(str(numero)):
        return False

    lista = []
    lista1 = []
    n = numero
    np = permutacion
    for i in range(len(str(permutacion))):
        lista.append(n%10)
        lista1.append(np%10)
        n //= 10
        np //=10

    lista.sort()
    lista1.sort()

    if lista == lista1:
        return True
    else:
        return False


flag = False

max = 100
min = 1
res = 0

while not flag:

    for i in range(min, (max//6)+1):
        mul = 2
        while esPermutacionNumero(i, mul*i) or mul == 7:
            mul += 1

        print i, mul, res
        if mul == 7:
            res = i
            flag = True
            break

    min = max
    max *= 10


