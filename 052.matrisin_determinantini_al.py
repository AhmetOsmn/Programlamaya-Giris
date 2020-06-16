def minor(array,i,j):
    c = array
    c = c[:i] + c[i+1:]
    for k in range(0,len(c)):
        c[k] = c[k][:j]+c[k][j+1:]
    return c

def det(array,n):
    if n == 1 :return array[0][0]
    if n == 2 :return array[0][0]*array[1][1] - array[0][1]*array[1][0]
    sum = 0
    for i in range(0,n):
        m = minor(array,0,i)
        sum =sum + ((-1)**i)*array[0][i] * det(m,n-1)
    return sum



matris = [[1,5,3],[2,4,7],[4,6,2]]

n = len(matris)

print(det(matris,n))
