def faktoriyel(sayi):
    if(sayi == 0):
        return 1

    elif(sayi == 1):
        return 1

    else:
        return faktoriyel(sayi - 1) * sayi



def kombinasyon(sayi1,sayi2):
    c = faktoriyel(sayi1)/(faktoriyel(sayi2) * (faktoriyel(sayi1-sayi2)))
    return c
n = int(input("n: "))
r = int(input("r: "))

komb = kombinasyon(n,r)
print("C(n,r) = {}".format(komb))
