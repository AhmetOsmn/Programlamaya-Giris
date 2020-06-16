import random

def en_buyuk(liste):
    eb = 0
    for i in liste:
        if(i >= eb):
            eb = i

    return eb

def en_kucuk(liste):
    ek = liste[0]
    for i in liste:
        if(i <= ek):
            ek = i

    return ek

liste = []
for i in range(10):
    liste.append(random.randint(1,51))

print(liste)

b = en_buyuk(liste)
k =  en_kucuk(liste)
fark = b - k
print(b,k,fark)
