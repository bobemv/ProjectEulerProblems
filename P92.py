__author__ = 'Roberto Moreno'


def funcion92(top, num=89):

    ochentaynueves = []
    ochentaynueves.append(89)

    for i in range(top):
        ciclo = i
        numeros = []
        print i
        while not ciclo in numeros:
            numeros.append(int(ciclo))
            ciclo = sum([(int(j))**2 for j in str(ciclo)])


            if ciclo in ochentaynueves:
                ochentaynueves.append(int(i))
                break

    return len(ochentaynueves) - 1; "89 repetido"


print funcion92(10000)
