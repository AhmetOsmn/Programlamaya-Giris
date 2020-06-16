with open("61_veri.txt","r") as file:
    sayilar = []
    for i in file:
        sayilar.append(i.split("\n")[0])

ters_ikili = []
ondaliklar = []
for i in sayilar:
    ters = []
    for j in i:
        ters.append(int(j))
    ters_ikili.append(list(reversed(ters)))


for i in ters_ikili:
    sayi = 0
    for j in range(len(i)):
        sayi += i[j] * (2**(j))

    ondaliklar.append(sayi)

for i in range(len(sayilar)):
    print("{} = {}".format(sayilar[i],ondaliklar[i]))
