__author__ = 'Roberto Moreno'

"Sweet Jesus Christ. Bless StackOverflow"
def isPalindrome(num):
    return str(num) == str(num)[::-1]

def reverseNumber(num):
    return int(str(num)[::-1])


lychrel = 0
for i in range(1, 10**4):
    contador = 1
    inverse = reverseNumber(i)
    suma = i + inverse

    while not isPalindrome(suma) and contador < 50:
        contador += 1
        inverse = reverseNumber(suma)
        suma = suma + inverse

    if contador == 50:
        lychrel += 1

    print i, suma, contador

print lychrel
