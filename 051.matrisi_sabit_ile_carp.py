"""
Matrisler 3x3 olarak aliniyor.
"""

def sabit_ile_carp(sabit,matris):
    smatris = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            smatris[i][j] = sabit*matris[i][j]

    for i in smatris:
        print(i)

m1 = [[1,3,2],[1,4,7],[1,2,2]]
sabit_ile_carp(5,m1)
