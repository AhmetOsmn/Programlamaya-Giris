def asal_mi(sayi):
    if(sayi == 1):
        return False
    if(sayi == 2):
        return True
    else:
        for i in range(2,int(sayi**(1/2))+1):
            if(sayi % i == 0):
                return False
        return True

def mersenne(n):
    return 2*n-1
mersenneler = []
for i in range(1,101):
    mersenneler.append(mersenne(i))

asal_mersenneler = []
for i in mersenneler:
    if(asal_mi(i)):
        asal_mersenneler.append(i)

print(asal_mersenneler)
