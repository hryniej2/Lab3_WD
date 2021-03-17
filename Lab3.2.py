import random
lista = random.sample(range(1, 100), 10)
print(lista)
lista2 = {x for x in lista if x % 2 ==0}
print(lista2)