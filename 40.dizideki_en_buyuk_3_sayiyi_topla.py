import random

def en_buyuk(liste):
    eb = 0
    for i in liste:
        if(i >= eb):
            eb = i

    return eb

liste = []
for i in range(10):
    liste.append(random.randint(1,51))

print(liste)
uc_buyuk = []
for i in range(3):
    eb = en_buyuk(liste)
    uc_buyuk.append(eb)
    liste.remove(eb)

print(uc_buyuk)
