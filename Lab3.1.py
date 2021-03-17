zakres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = {1-x for x in zakres}
B = {4**y for y in range(8)}
C = {z for z in B if z % 2 == 0}
print(C)
print(B)
print(A)
#nie mam pojęcia czemu wychodza niepoprawne wyniki.