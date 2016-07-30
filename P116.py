__author__ = 'Roberto Moreno'

def funcion116(numero):

    suma = 0
    for i in range(2, 5):
        tabla = []

        tabla.append(0)
        for j in range(1, i):
            tabla.append(1)

        tabla.append(2)

        for j in range(i+1, numero):
            tabla.append(recursivo116(j, i, tabla))

        suma += (recursivo116(numero, i, tabla) - 1); "<- La funcion cuenta con una combinacion donde no hay tiles puestas. En Euler no la cuentan."


    return suma



def recursivo116(numero, color=2, tabla = []):

    return tabla[numero-1] + tabla[numero-color]


print funcion116(50)

