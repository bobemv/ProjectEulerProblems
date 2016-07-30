__author__ = 'Roberto Moreno'

def funcion117(numero, inicio):

    tabla = []
    "Hard code best code"
    tabla.append(0)
    tabla.append(1)
    tabla.append(2)
    tabla.append()

    if numero < (2*inicio)+1:
        return tabla[numero-1]

    for i in range((2*inicio)+1, numero):
        tabla.append(recursion117(i, tabla, inicio))

    return recursion117(numero, tabla, inicio), tabla



def recursion117(numero, tabla, inicio):

    suma = 0
    for i in range(2, numero-1):
        "Piezas de 2, 3 y 4 tiles"
        suma += (tabla[i-1] - 1)

    suma += (numero - 1)

    for i in range(1, numero-3):
        suma -= tabla[i]

    return tabla[numero-2] + suma


print funcion117(5, 2)