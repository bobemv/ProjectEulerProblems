import math
__author__ = 'Roberto Moreno'


def sumaCifrasFactorial(numero):
    x = math.factorial(numero)
    suma = 0

    while not x <= 0:
        suma += x % 10
        x /=10

    print suma
print sumaCifrasFactorial(100)