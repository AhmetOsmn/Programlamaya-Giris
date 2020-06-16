"""
Bir matrisin tersini alirken determinantinin != 0 olduguna dikkat etmeliyiz.
detA == 0 ise Tersi alinamayacaktir.
Matrisler 3x3 olarak aliniyor.
"""

def birim_matris():
    b_matris = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            if(i == j):
                b_matris[i][j] = 1
            else:
                b_matris[i][j] = 0
    return b_matris

def donustur(matris,birim_matris):
    for i in range(3):
        d = matris[i][i]


        for j in range(3):
            matris[i][j] = (matris[i][j])/d
            birim_matris[i][j] = (birim_matris[i][j])/d

        for j in range(3):
            if(j != i):
                k = matris[j][i]
                for x in range(3):
                    matris[j][x] = matris[j][x]-(matris[i][x]*k)
                    birim_matris[j][x] = birim_matris[j][x]-(birim_matris[i][x]*k)

    return birim_matris


matris = [[1,0,5],[2,1,6],[3,4,0]]
birim_matrisi = birim_matris()
#print(birim_matrisi)
matrisin_tersi = donustur(matris,birim_matrisi)

for i in matrisin_tersi:
    print(i)
