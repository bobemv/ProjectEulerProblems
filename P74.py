__author__ = 'Roberto Moreno'

import math

for i in range(1, 10**3):
    num = i
    fac = math.factorial(num)
    contador = 1

    while (fac != 169 and fac != 145 and fac != 871 and fac != 872 and fac != 1 and fac != 2):
        contador += 1
        num = fac
        l = [int(j) for j in str(fac)]
        fac = 0
        for j in l:
            fac += math.factorial(j)
        print "-> ", fac
    print i, contador


