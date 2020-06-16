def asal_mi(sayi):
    if(sayi == 0):
        return False
    if(sayi == 1):
        return False
    if(sayi == 2):
        return True
    else:
        for i in range(2,int(sayi**(1/2)+1)):
            if(sayi % i == 0):
                return False
        return True

asallar = []
i = 0
while(len(asallar) < 20):
    if(asal_mi(i)):
        asallar.append(i)
        i += 1
    else:
        i += 1
print(asallar)
