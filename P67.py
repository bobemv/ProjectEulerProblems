__author__ = 'Roberto Moreno'
from time import clock

time = clock()
f = open("P67Data.txt", "r")

piramide = [map(int,line.split(' ')) for line in f if line.strip() != "" ]

print piramide.__len__()

n = piramide.__len__()


i = n-2
while i >= 0:
    for j in range(0, i+1):
        numero = piramide[i][j]
        x = piramide[i+1][j]
        y = piramide[i+1][j+1]
        if x > y:
            piramide[i][j] += x
        else:
            piramide[i][j] += y

    i-=1

print piramide[0][0]

time2 = clock()

print (time2-time)*1000.0