def matris_carp(a,b):
    c = [[0,0],[0,0]]
    for i in range(2):
       for j in range(2):
           for k in range(2):
               c[i][j] = a[i][k]*b[k][j] + c[i][j]

    for i in c:
        print(i)


m1 = [[1,2],[3,4]]
m2 = [[5,6],[7,8]]
matris_carp(m1,m2)
