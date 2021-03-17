Produkty = {"Mandarynka": "gramy", "Baton": "sztuki", "Ser": "gramy", "telefon": "sztuki", "Lizak": "sztuki",}
Produkty_Sztuki = {a: b for a,b in Produkty.items() if b == "sztuki"}
print(Produkty_Sztuki)