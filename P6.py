__author__ = 'Roberto Moreno'

def sumaCuadrados(maximo):
    return maximo*(maximo+1)*(2*maximo+1)/6

def sumaAlCuadrado(maximo):
    return (maximo*(maximo+1)/2)**2


print sumaCuadrados(10), sumaAlCuadrado(10)

print sumaAlCuadrado(100)-sumaCuadrados(100)