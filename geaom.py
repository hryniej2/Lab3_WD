def wyraz_n(a1, n, q):
    wyraz = a1 * (q ** (n-1))
    return wyraz


def suma_wyraz(a1, n, q):
    if q == 1:
        suma = a1 * n
    else:
        suma = a1 * ((1 - q ** n) / (1 - q))
    return suma


def srdk_wyraz(x, z):
    y = x * z
    for i in range(y):
        if i * i == y:
            y = i
    return y