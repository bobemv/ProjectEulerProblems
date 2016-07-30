__author__ = 'Roberto Moreno'

import math

def esPrimo(numero):
    if numero == 1:
        return False
    if numero<4:
        return True
    if numero%2 == 0:
        return False
    if numero<9:
        return True
    if numero%3 == 0:
        return False
    raiz = math.sqrt(numero)
    funcion = 5
    while funcion <= raiz:
        if numero%funcion == 0:
            return False
        if numero%(funcion+2) == 0:
            return False
        funcion+=6

    return True


def squareFreeOnPascalTriangle(rows=8):

    numeros = set()
    row = [1]

    numeros.add(1)

    for i in range(2, rows+1):
        nuevaRow = []

        "Si es par, noy hay numero central"
        if i % 2 == 0:
            for j in range(len(row)):
                izquierda = j - 1
                derecha = j

                if izquierda < 0:
                    nuevaRow.append(row[derecha])
                else:
                    nuevaRow.append(row[izquierda]+row[derecha])
        else:
            for j in range(len(row)+1):
                izquierda = j - 1
                derecha = j

                if izquierda < 0:
                    nuevaRow.append(row[derecha])
                elif derecha >= len(row):
                    nuevaRow.append(2*row[len(row)-1])
                else:
                    nuevaRow.append(row[izquierda]+row[derecha])

        row = nuevaRow[:]
        numerosDistintos = set(nuevaRow)
        numeros = numeros.union(numerosDistintos)


    squarefree = []

    for i in list(numeros):
        primo = 2
        flag = True
        while primo <= math.sqrt(i):
            while not esPrimo(primo):
                primo+=1

            if i % (primo**2) == 0:
                flag = False
                break

            primo += 1


        if flag and i % primo**2 != 0:
            squarefree.append(i)

    return squarefree



a = squareFreeOnPascalTriangle(rows=8)
a.sort()
print sum(a), a


