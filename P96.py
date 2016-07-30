__author__ = 'Roberto Moreno'
import time

def solucionadorSudoku(sudoku, depth = 1):

    "Cada subcuadrado del sudoku lo almacenamos en una lista"
    "listas = [i for i in range(9), [j for j in sudoku[i*9:(i+1)*9]]]"

    flag = False
    if 0 in sudoku:

        for i in range(len(sudoku)):
            numero = sudoku[i]
            if numero == 0:
                cuadrado = (i // 27)*3 + (i % 9)//3; "Posicion cuadrado de 3x3 del numero"
                columna = i%9
                fila = i//9
                while True:
                    numero += 1
                    flag = False
                    if numero > 9:
                        sudoku[i] = 0
                        return False
                    else:
                        for j in range(9):
                            if sudoku[columna+j*9] == numero:
                                flag = True
                                break
                            if sudoku[fila*9+j] == numero:
                                flag = True
                                break
                            n = sudoku[(cuadrado//3)*27+(cuadrado%3)*3+(j//3)*9+j%3]
                            if sudoku[(cuadrado//3)*27+(cuadrado%3)*3+(j//3)*9+j%3] == numero:

                                flag = True
                                break

                        if flag:
                            continue

                        sudoku[i] = numero

                        if solucionadorSudoku(sudoku, depth+1):
                            if depth == 1:

                                return sudoku
                            else:
                                return True




    else:
        return sudoku


def printSudoku(sudoku):
    for i in range(9):
        print sudoku[i*9:(i+1)*9]
    return


sudoku = [0, 0, 3, 0, 2, 0, 6, 0, 0, 9, 0, 0, 3, 0, 5, 0, 0, 1, 0, 0, 1, 8, 0, 6, 4, 0, 0, 0, 0, 8, 1, 0, 2, 9, 0, 0,
          7, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 6, 7, 0, 8, 2, 0, 0, 0, 0, 2, 6, 0, 9, 5, 0, 0, 8, 0, 0, 2, 0, 3, 0, 0, 9,
          0, 0, 5, 0, 1, 0, 3, 0, 0]

f = open("P96Data.txt", 'r')

listaSudokus = []
nuevo = []

f.readline()

for line in f:
    if line.find("Grid") >= 0:
        listaSudokus.append(nuevo)
        nuevo = []
        continue

    for c in line:
        if c == "\n":
            continue
        nuevo.append(int(c))

listaSudokus.append(nuevo)

print listaSudokus


suma = 0

t1 = time.clock()

i = 0
for sudoku in listaSudokus:
    print i
    sudoku = solucionadorSudoku(sudoku)
    a = map(str,(sudoku[i] for i in range(3)))
    suma += int("".join(a))
    print i, suma
    i+=1

print "Resultado: ", suma, "en ", time.clock()-t1
