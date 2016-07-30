__author__ = 'Roberto Moreno'

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


def funcion(maximo):




