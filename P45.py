__author__ = 'RobertoMoreno'

"Solucion: (1533776805, 55385, 31977, 27693)"
def numeroTriPenYHex(hexagonal=144, pentagonal = 165, triangular = 285):

    flag = False

    contadorH = hexagonal
    contadorP = pentagonal
    contadorT = triangular

    while not flag:
        contadorH += 1
        h = contadorH*(2*contadorH-1); "Buscamos el numero hexagonal"
        p = 0
        while h >= p:
            contadorP += 1
            p = contadorP*(3*contadorP-1)/2
            if h == p:
                t = 0
                while h >= t:
                    contadorT += 1
                    t = contadorT*(contadorT+1)/2
                    if h == t:
                        flag = True
                        break


                break

    return h, contadorT, contadorP, contadorH


print numeroTriPenYHex()
