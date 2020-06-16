"""
Matrisler 3x3 olarak aliniyor.
"""
def matris_topla(m1,m2):
    smatris = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            smatris[i][j] = m1[i][j] + m2[i][j]

    for i in smatris:
        print(i)

m1 = [[1,3,2],[1,0,0],[1,2,2]]
m2 = [[0,0,5],[7,5,0],[2,1,1]]
matris_topla(m1,m2)
