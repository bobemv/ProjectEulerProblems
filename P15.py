from time import clock
__author__ = 'Roberto Moreno'


def caminosRejilla(altura, ancho, valores, flag=True):
   "Total caminos posibles en una rejilla yendo solo de derecha y abajo"
   suma = 0
   if flag != True and altura == ancho:
       return valores[altura-1]
   elif flag == True and altura == ancho:
       return 2*caminosRejilla(altura-1, ancho, valores, flag=False)

   if altura == 0:
       return 1

   return caminosRejilla(altura-1, ancho, valores, flag=False) + caminosRejilla(altura, ancho-1, valores, flag=False)

def caminosRejillav2(dimension):

    valores = []
    valores.append(2)

    i = 2
    while i <= dimension:
        time1 = clock()
        valores.append(caminosRejilla(i, i, valores))
        time2 = clock()
        print "Dimension", i, "x", i, "calculada. Tiempo = ", (time2-time1), "s  ", (time2-time1)*1000.0, "ms"
        i+=1

    return valores


def caminosRejillas(altura, ancho, valores):
   "Total caminos posibles en una rejilla yendo solo de derecha y abajo"
   suma = 0
   i = 0
   while i<=altura-1:
       suma+=valores[altura-1][i]
       valores[altura][i] = suma
       i+=1

   valores[altura][ancho] = 2*suma

   return

def caminosRejillasv2(dimension):

    valores = [[0 for j in range(0, dimension+1)] for i in range(0, dimension+1)]
    valores[0][0] = 1
    valores[1][0] = 1
    valores[0][1] = 1
    valores[1][1] = 2

    i = 1
    while i <=dimension:
        time1 = clock()
        caminosRejillas(i, i, valores)
        time2 = clock()
        print "Dimension", i, "x", i, "calculada. Tiempo = ", (time2-time1), "s  ", (time2-time1)*1000.0, "ms"
        i+=1

    return [valores[i][i] for i in range(0, dimension+1)]


print caminosRejillasv2(20)
