def ramanujan_mi(sayi):
    liste = []
    for i in range(int(sayi**(1/3))+2):
        k = i**3
        for j in range(int(sayi**(1/3))+2):
            m = j**3
            if(k+m == sayi):
                demet = (i,j)
                liste.append(demet)
    if(len(liste) != 0):
        liste.pop()
        liste.pop()
    return liste


for i in range(4):
    sayi1 = int(input("Sayi: "))

    elemanlari = ramanujan_mi(sayi1)
    if(len(elemanlari) == 0):
        print("Sayi Ramanujan sayisi degil")
    else:
        print("Sayi Ramanujan sayisidir,olustugu sayilar: ")
        for i in elemanlari:
            print(i)
