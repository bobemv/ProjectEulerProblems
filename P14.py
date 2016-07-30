__author__ = 'Roberto Moreno'

def mayorSecuenciaCollatz(cota):
    maximo = 0
    contadorMaximo = 0;

    for i in range(1, cota+1):
        x = i
        contador = 1
        while x > 1:
            if x%2 == 0:
                x = x/2
            else:
                x = (3*x)+1

            contador+=1

        if contador > contadorMaximo:
            maximo = i
            contadorMaximo = contador

    return maximo

print mayorSecuenciaCollatz(1000000)
