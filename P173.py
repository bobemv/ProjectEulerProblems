__author__ = 'Roberto Moreno'

def funcion173(tiles):

    bordes = []
    maneras = 0
    n = 1
    contador = 1

    while n <= tiles:
        bordes.append(n)
        maneras += 1
        contador += 1
        n = contador * 4 - 4

    longitud = len(bordes)
    print bordes

    for i in range(2, longitud):
        for j in range(i+1, longitud):
            if sum(bordes[i:j+1]) <= tiles:
                print i, j+1, sum(bordes[i:j+1]), maneras
                maneras += 1
            else:
                break

    return maneras


def funcion173v2(tiles):

    maneras = 0
    print maneras

    n = 4
    m = 3
    ms = 4

    while ms <= (tiles//2)+2:
        ms += 8
        ns = ms

        while ns <= tiles:
            print m, ms, ns
            maneras += 1
            ns += ns + 8
        m += 1

    ms = 8
    m = 3
    while m < (tiles//2)+2:
        ns = ms

        while ns <= tiles:
            print m, ms, ns
            maneras += 1
            ns += ns + 8
        m += 1
        ms += 8

    return maneras

print funcion173v2(100)