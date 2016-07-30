__author__ = 'Roberto Moreno'

def ultimosDigitosExponencial(base, exponente, digitos, multiplicacion=1, suma=0, resta=0):

    total = 1

    for i in range(exponente):
        total *= base
        cadena = str(total)
        if len(cadena) > digitos:
            total = int(cadena[1:])

    orig = total
    for i in range(multiplicacion-1):
        total += orig
        cadena = str(total)
        if len(cadena) > digitos:
            total = int(cadena[1:])

    total += suma - resta

    cadena = str(total)
    if len(cadena) > digitos:
        total = int(cadena[1:])

    return total


a = ultimosDigitosExponencial(2, 7830457, 10, multiplicacion=28433, suma=1)

print a