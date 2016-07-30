__author__ = 'Roberto Moreno'
import math;
def numeroFibonacci(n):
    "0, 1, 1, 2, 3, 5, 8, 13, 21, 34"
    aureo = (1 + math.sqrt(5))/2;
    return (aureo**n-(1-aureo)**n)//math.sqrt(5);

fibonacci = 0;
n = 3;
max = 4000000;
suma = 0;

while fibonacci < max:
    fibonacci = numeroFibonacci(n);
    suma += fibonacci;
    print "Numero Fibonacci ", n, ": ", fibonacci, ". Suma total: ", suma;
    n += 3;

suma -= fibonacci;
print "Suma de numeros de Fibonacci pares que no excedan 4.000.000: ", suma;




