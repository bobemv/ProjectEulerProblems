__author__ = 'Roberto Moreno'

def sumasDias(inicio, fin, dia):
    diaInicio = 0
    for i in range(1900, inicio):
        anio = 365
        if (i%400 == 0):
            anio = 366

        diaInicio += anio%7
        if diaInicio>6:
            diaInicio = diaInicio%7

    "Tenemos el dia inicial ahora (lunes=0, martes=1, miercoles=2...)"

    suma = 0

    for i in range(inicio, fin+1):
        feb = 28
        if i%400 or i%4 == 0:
            feb = 29

        for j in range(0, 12):

            print "Anio:", i, ", Mes:", j, "Primer dia:", diaInicio
            if(diaInicio == dia):
                suma += 1

            if(j==1):
                diaInicio += feb%7
            elif j==8 or j==3 or j==5 or j==10:
                diaInicio += 30%7
            else:
                diaInicio += 31%7

            if diaInicio>6:
                diaInicio = diaInicio%7

    return suma

print sumasDias(1901, 2000, 6)
"No se por que es incorrecto"

