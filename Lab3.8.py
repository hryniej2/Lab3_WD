def zakupy(** produkty):
    suma = 0
    liczba = 0
    for i in produkty:
        liczba += 1
        suma += produkty[i]
    print("Liczba produktów: " + str(liczba) + "\n" + "Suma: " + str(suma))
zakupy(baton=2.50, chleb=2, bułka=1.99, colka=3.59)