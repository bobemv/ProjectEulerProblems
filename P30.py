__author__ = 'Roberto Moreno'


potencia = 5
total = 0

"Numero magico! 1 millon por ejemplo. Problema sin solucionar: limite superior del bucle para parar de buscar numeros"
for i in range(10, 1000000):
    lista = [int(j) for j in str(i)]
    suma = 0
    for j in lista:
        suma += j**potencia

    if suma == i:
        print i
        total += i



print total