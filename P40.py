__author__ = 'Roberto Moreno'

"Solucion: 210"
def cuentaDigitos(posicion):

    contador = 0
    n = 1
    while contador < posicion:
        tabla = list(str(n))
        if contador + len(tabla) >= posicion:
            digito = int(tabla[posicion - contador -1])

        contador += len(tabla)
        n += 1

    return digito

mul = cuentaDigitos(10**(0))*cuentaDigitos(10**(1))*cuentaDigitos(10**(2))*cuentaDigitos(10**(3))*cuentaDigitos(10**(4))*cuentaDigitos(10**(5))*cuentaDigitos(10**(6))

print mul

