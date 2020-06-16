import random
liste = []
for i in range(5):
    liste.append(random.randint(1,10))

print(liste)

carpimlar = 1
for i in liste:
    carpimlar = carpimlar * i

gort = carpimlar**(1/len(liste))
print("Listenin geometrik ortalamasi: {}".format(gort))
