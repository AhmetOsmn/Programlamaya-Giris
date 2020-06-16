matris_boyutu = int(input("Kare Matrisin Boyu: "))


matris = []
for i in range(matris_boyutu):
    matris.append([0]*matris_boyutu)

#print(matris)

x_duzlemi = 0
y_duzlemi = 0
toplam = 1

arttir = True
for i in range(matris_boyutu):
    matris[x_duzlemi][y_duzlemi] = toplam
    #print(matris)
    if(arttir):
        while(x_duzlemi + 1 < matris_boyutu and matris[x_duzlemi + 1][y_duzlemi] == 0):
            x_duzlemi += 1
            toplam += 1
            matris[x_duzlemi][y_duzlemi] = toplam

        while(y_duzlemi + 1 < matris_boyutu and matris[x_duzlemi][y_duzlemi + 1] == 0):
            y_duzlemi += 1
            toplam += 1
            matris[x_duzlemi][y_duzlemi] = toplam

    else:
        while(x_duzlemi > 0 and matris[x_duzlemi - 1][y_duzlemi] == 0 ):
            x_duzlemi -= 1
            toplam += 1
            matris[x_duzlemi][y_duzlemi] = toplam

        while (y_duzlemi > 0 and matris[x_duzlemi][y_duzlemi - 1] == 0):
            y_duzlemi -= 1
            toplam += 1
            matris[x_duzlemi][y_duzlemi] = toplam

    arttir = not(arttir)

for i in range(matris_boyutu) :
    for j in range(matris_boyutu):
        print(matris[j][i],end="")
    print("")
