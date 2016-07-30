__author__ = 'Roberto Moreno'

def permutacionesNumero(numero):
    lista = []
    n = numero
    for i in range(len(str(numero))):
        lista.append(n%10)
        n //= 10

    lista.sort()

    lista1 = []

    perm = recursividad(lista1, lista)

    return perm

def recursividad(lista, restantes, permutaciones=[]):

    if restantes.__len__() == 0:
        permutaciones.append(lista)
        return permutaciones

    for i in restantes:
        lista1 = list(lista)
        lista1.append(i)
        lista2 = list(restantes)
        lista2.remove(i)
        recursividad(lista1, lista2)

    return permutaciones

perm = permutacionesNumero(1234567890)
print perm[999999]


