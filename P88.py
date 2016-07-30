def productorio(*numeros):
    ret = 1;
    for x in numeros:
        ret *= x;

    return ret;

def sumatorio(*numeros):
    ret = 1;
    for x in numeros:
        ret += x;

    return ret;

max = 6;

sumas = set;

for i in range(max):
    productos = [];
    sumandos = [];
    productos = [1 for x in range(i)];
    sumandos = productos[:];
    suma = 0;
    multi = 1;
    flag = 1;
    while suma != multi:
        newProductos = [];
        P = [];
        for j in range(i):
            newProductos = productos[:];
            newProductos[j] += 1;
            if flag == 1:
                multi = productorio(newProductos);
                P = newProductos[:];
            else:
                multi2 = productorio(newProductos);
                if multi2 < multi:
                    multi = multi2;
                    P = newProductos[:];
            flag = 0;

        productos = P;
        sumandos = productos[:];
        suma = sumatorio(sumandos);
        multi = productorio(productos);
        flag = 1;
    sumas.add(suma);

resultado = sumatorio(list(sumas));

print resultado;