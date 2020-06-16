import random
def tekler(liste):
    tekler = []
    for i in liste:
        if(i%2 != 0):
            tekler.append(i)
    return tekler

liste = []
for i in range(10):
    liste.append(random.randint(1,20))
print(liste)

tekler = tekler(liste)

carpimlar = 1
for i in tekler:
    carpimlar = carpimlar * i

tgort = carpimlar**(1/len(tekler))
print("Listede ki tek sayilarin geometrik ortalamasi: {}".format(tgort))
