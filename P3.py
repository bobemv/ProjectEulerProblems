__author__ = 'roberto'
"Idea -> En C, dos hilos de procesador: en uno, se va buscando el factor aumentando de 1 en 1"
" mientras el otro hilo va reduciendo el pool (buscamos maximo factor de 1000. Si es divisible por 2, entonces"
" solo tenemos que buscar hasta 500 ahora (se podria incluso reducir aun mas)"
def maximoFactorNumero(numero):
    "No hace lo que pide el problema"
    ret = 1;
    a = 1;
    for i in range(1, numero):
        if numero%i == 0:
            ret = i
    return ret;

def maximoFactorNumerov2(numero):
    "Usando recursion = menos eficiente"
    ret = 1;
    for i in range(2, numero+1):
        if numero%i == 0:
            print i;
            ret = i;
            if numero/i != 1:
                ret = maximoFactorNumerov2(numero/i);
            break;

    return ret;

def maximoFactorNumerov3(numero):
    "Funciona perfecto para numeros 'grandes' como 600851475140 porque"
    "esta puesto para que con este algoritmo se encuentren los factores rapidamente"
    flag = False;
    i = 2;
    ret = 1;
    iter = numero;

    while not flag:
        if iter%i == 0:
            iter /=i
            if iter == 1:
                ret = i;
                flag = True;
        i += 1
    return ret


print maximoFactorNumerov3(600851475140);