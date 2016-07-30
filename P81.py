__author__ = 'Roberto Moreno'

import time

def formatMatrix(l):
    for i in l:
        print i

    print ""

def funcion81():
    c = time.clock()
    f = open('P81Data.txt', 'r')

    l = [ map(int,line.split(',')) for line in f if line.strip() != "" ]

    i = 0
    j = 0

    n = len(l)

    for j in range(1, n):
        l[0][j] += l[0][j-1]
        l[j][0] += l[j-1][0]

    for i in range(1, n):

        if l[i-1][i] < l[i][i-1]:
            l[i][i] += l[i-1][i]
        else:
            l[i][i] += l[i][i-1]

        for j in range(i+1, n):
            if l[i-1][j] < l[i][j-1]:
                l[i][j] += l[i-1][j]
            else:
                l[i][j] += l[i][j-1]

        for j in range(i+1, n):
            if l[j-1][i] < l[j][i-1]:
                l[j][i] += l[j-1][i]
            else:
                l[j][i] += l[j][i-1]



    print l[n-1][n-1], time.clock()-c


"Soluciones en Euler (mas sencillo): recorrer toda la tabla ('i' a 'j' y comprobar su " \
"arriba e izquierda cual es mayor). Para cuando llegue al final tendra la solucion " \
"se puede recorrer la tabla asi ya que el camino solo puede ir abajo y a la derecha"