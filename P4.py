__author__ = 'Roberto Moreno'

def esPalindromo(numero):
    invertido = 0;
    derecho = numero;
    while derecho >= 1:
        invertido *= 10
        invertido += derecho % 10
        derecho //= 10

    if invertido == numero:
        return True
    return False

def maxPalindromoProdDosNumTresCifr():
    ret = 1;
    for a in range(10, 1000):
        for b in range(10, 1000):
            mul = a*b
            if esPalindromo(mul):
                if mul >= ret:
                    ret = mul
                    p = a, b

    return ret, p

print maxPalindromoProdDosNumTresCifr()