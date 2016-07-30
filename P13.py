__author__ = 'roberto'

f = open("P13Data.txt", "r")

l = [ map(int,line.split(' ')) for line in f if line.strip() != "" ]

print l
suma = 0
for i in range(l.__len__()):
    suma += l[i].pop()

print suma