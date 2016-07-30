__author__ = 'Roberto Moreno'

def sumaDiagonalesEspiral(tamanio):
    valor = 1
    if tamanio%2 == 0:
        valor = -1
    elif (tamanio == 1):
        valor = 1
    else:
        n = tamanio
        while n>1:
            i = n-1
            for j in range(0, 4):
                valor += n**2 - j*i
            n -= 2
    return valor

print sumaDiagonalesEspiral(1001)
