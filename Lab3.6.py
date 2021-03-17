def ciag(a=1, b=4, ile=10):
    iloczyn = a
    for i in range(ile):
            iloczyn *= b
    return iloczyn
print(ciag())