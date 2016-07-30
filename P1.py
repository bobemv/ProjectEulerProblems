
def sumaDivisores(n, numeros = 999):
    "Se calculan el numero de divisores en el"
    "intervalo de cierto n y se realiza el sumatorio"
    numDiv = numeros // n;
    return n*(numDiv*(numDiv+1))/2;
__author__ = 'Roberto Moreno'

"Solucion mala"
resultado = 0;
for i in range(1000):
    "En range(1000) va de 0 a 999"
    if ((i % 5) == 0) or ((i % 3) == 0):
        resultado += i;
print resultado;

"Solucion buena"

print sumaDivisores(3)+sumaDivisores(5)-sumaDivisores(15);

