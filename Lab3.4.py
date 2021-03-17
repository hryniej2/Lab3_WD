def kwadratowy(a, b, c):
    warunek1 = a**2 + b**2
    warunek2 = c**2
    if warunek1 == warunek2:

        return ("Prostokątny")


    else:
        return ("Nie prostokątny")

print(kwadratowy(3, 4, 5))
