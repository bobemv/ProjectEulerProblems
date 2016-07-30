__author__ = 'Roberto Moreno'

f = open("P22Data.txt", "r")

lista = [map(str,line.split('","')) for line in f if line.strip() != "" ]

lista2 = lista[0]

lista2.sort()


lista2.pop(0)


print lista2
suma = 0;
print len(lista2)
for i in range(len(lista2)):
    val = lista2[i]
    suma2= 0
    for j in range(len(val)):

        suma2+=ord(val[j])-64

    suma+=suma2*(i+1)
    print i, ":",val, suma2, "*", i+1, "=", suma2*(i+1), ",", suma

print suma

print lista2[937]
