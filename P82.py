__author__ = 'Roberto Moreno'

import time
import numpy

def formatMatrix(l):
    for i in l:
        print i

    print ""

def funcion82():

    f = open('P81DataPrueba.txt', 'r')
    l = [ map(int,line.split(',')) for line in f if line.strip() != "" ]

    i = 0
    j = 0

    n = len(l)


    formatMatrix(l)
    for j in range(1, n-1):

        if l[0][j-1] < l[1][j]:
            l[0][j] += l[0][j-1]
        else:
            l[0][j] += l[1][j]

        for i in range(1, n-1):

            up = l[i-1][j]
            left = l[i][j-1]
            down = l[i+1][j]

            if up < left and up < down:
                l[i][j] += up
            elif left < down and left < up:
                l[i][j] += left
            else:
                l[i][j] += down

        if l[n-1][j-1] < l[n-2][j]:
            l[n-1][j] += l[n-1][j-1]
        else:
            l[n-1][j] += l[n-2][j]

        formatMatrix(l)

    for i in range(n):
        l[i][n-1] += l[i][n-2]

    formatMatrix(l)

    l = numpy.array(l)

    print min(l[:,n-1])

def funcion82v2():
    f = open('P81DataPrueba.txt', 'r')
    l = [ map(int,line.split(',')) for line in f if line.strip() != "" ]

    n = len(l)


    formatMatrix(l)
    listaPasan = [i for i in range(n)]

    for j in range(1, n-1):

        for i in listaPasan:
            l[i][j] += l[i][j-1]

        listaPasan = []

        if l[1][j] < l[0][j+1]:
            l[i][j] += l[1][j]
        else:
            listaPasan.append(0)

        for i in range(1, n-1):
            up = l[i-1][j]
            right = l[i][j+1]
            down = l[i+1][j]

            if up < right and up < down:
                l[i][j] += up
            elif down < right and down < up:
                l[i][j] += down
            else:
                listaPasan.append(i)
                pass

        if l[n-2][j] < l[n-2][j+1]:
            l[i][j] += l[n-2][j]
        else:
            listaPasan.append(n-1)

        formatMatrix(l)
        print listaPasan

    for i in listaPasan:
        l[i][n-1] += l[i][n-2]

    formatMatrix(l)

    l = numpy.array(l)

    print min(l[:,n-1])


"Shit implementation. No funciona."
def funcion82v3():
    f = open('P81DataPrueba.txt', 'r')
    l = [ map(int,line.split(',')) for line in f if line.strip() != "" ]

    n = len(l)

    marcadores = [[[k for k in range(4)] for j in range(5)] for i in range(5)]

    for i in marcadores[0]:
        i.remove(0)

    for i in marcadores[n-1]:
        i.remove(2)

    for i in range(n):
        marcadores[i][1].remove(1)

    formatMatrix(l)

    for i in range(n):
        l[i][1] += l[i][0]
        "Quitar izquierdas a columna 1"

    formatMatrix(l)

    for j in range(1, n-1):

        for i in range(n):
            "Default: Right"
            min = l[i][j+1]
            direccion = 3
            for dir in marcadores[i][j]:
                if dir == 0:
                    "Up"
                    if min > l[i-1][j]:
                        min = l[i-1][j]
                        direccion = 0
                elif dir == 1:
                    "Left"
                    if min > l[i][j-1]:
                        min = l[i][j-1]
                        direccion = 1
                elif dir == 2:
                    "Down"
                    if min > l[i+1][j]:
                        min = l[i+1][j]
                        direccion = 2
                elif dir == 3:
                    "Right"
                    if min > l[i][j+1]:
                        min = l[i][j+1]
                        direccion = 3
                else:
                    pass

            if direccion == 0:
                "Al de arriba le quitamos abajo"
                marcadores[i-1][j].remove(2)
            elif direccion == 1:
                "Al de la izquierda le quitamos derecha (?)"
                marcadores[i][j-1].remove(3)
            elif direccion == 2:
                "Al de abajo le quitamos arriba"
                marcadores[i+1][j].remove(0)
            elif direccion == 3:
                "Al de la derecha le quitamos izquierda"
                marcadores[i][j+1].remove(1)
            else:
                pass

            l[i][j] += min
        formatMatrix(l)

    for i in range(n):
        l[i][n-1] += l[i][n-2]
        "Quitar izquierdas a columna 1"

    formatMatrix(l)

    l = numpy.array(l)

"Megacaca implementacion, poor thought, poor efficiency. EDIT: Esto es basura."

def funcion82v4():
    f = open('P81DataPrueba.txt', 'r')
    l = [ map(int,line.split(',')) for line in f if line.strip() != "" ]

    n = len(l)


    formatMatrix(l)
    caminos = [l[i][0]+l[i][1] for i in range(n)]


    print caminos

    for j in range(1, n-1):


        for i in range(n):

            temporal = [l[aux][j+1] for aux in range(n)]
            anteriores = [aux for aux in range(n)]
            indice = i

            "Para arriba"
            for k in range(i-1, -1, -1):
                suma = 0
                for m in range(indice-1, k-1, -1):
                    suma += l[m][j]
                suma += l[k][j+1]
                print "Columna: ", j, "Indice: ", i," a ", k, "Suma: ", suma
                if suma < temporal[k]:
                    temporal[k] = suma
                    anteriores[k] = i

            "Para abajo"
            for k in range(i+1, n):
                suma = 0
                for m in range(indice+1, k+1):
                    suma += l[m][j]
                suma += l[k][j+1]
                print "Columna: ", j, "Indice: ", i," a ", k, "Suma: ", suma
                if suma < temporal[k]:
                    temporal[k] = suma
                    anteriores[k] = i

        print "Temporal: ", temporal, "Caminos: ", caminos
        for i in range(n):
            temporal[i] += caminos[anteriores[i]]

        caminos = list(temporal)
        print "Caminos finales: ", caminos


    formatMatrix(l)

    print caminos



"OKOK I MOTHERFUCKING GOT THIS. 4 AM IDEA HERE IT GOES. EDIT: Demasiado bonito para ser cierto"

def funcion82v5():
    f = open('P81DataPrueba.txt', 'r')
    l = [ map(int,line.split(',')) for line in f if line.strip() != "" ]

    n = len(l)


    formatMatrix(l)
    caminos = [l[i][0] for i in range(n)]


    print caminos

    for j in range(1, n-1):

        for i in range(n):

            minimo = caminos[i] + l[i][j]

            "Para arriba"
            suma = l[i][j]
            for k in range(i-1, -1, -1):
                suma += l[k][j]

                if minimo > (caminos[k] + suma):
                    minimo = caminos[k] + suma

            "Para abajo"
            suma = l[i][j]
            for k in range(i+1, n):
                suma += l[k][j]

                if minimo > (caminos[k] + suma):
                    minimo = caminos[k] + suma

            caminos[i] = minimo

        print caminos

    print [caminos[i] + l[i][n-1] for i in range(n)]
    print min([caminos[i] + l[i][n-1] for i in range(n)])


funcion82v5()