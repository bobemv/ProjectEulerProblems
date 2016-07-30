__author__ = 'Roberto Moreno'

set = set()
for i in range(2, 101):
    for j in range(2, 101):
        set.add(i**j)

lista = list(set)
lista.sort()

print lista
print len(lista)
