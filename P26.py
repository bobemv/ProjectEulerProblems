__author__ = 'Roberto Moreno'
import decimal

def funcion(numero):

    "Creo que no estoy seguro de por que funciona"
    maximo = 0
    maxNum = 0

    for i in range(1, numero+1):
        contador = 0
        lista = []
        pordiez = 10
        while not ((pordiez // i, pordiez%i) in lista):
            if pordiez % i == 0:
                contador += 1
                break

            lista.append((pordiez//i, pordiez%i))
            pordiez = 10*(pordiez % i)

            contador += 1

        if contador > maximo:
            maxNum = i
            maximo = contador
            print i, maximo, lista

    return maxNum, maximo


print funcion(1000)
