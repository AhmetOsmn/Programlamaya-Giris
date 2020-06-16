def faktoriyel(sayi):
    if(sayi == 0):
        return 1

    elif(sayi == 1):
        return 1

    else:
        return faktoriyel(sayi-1)*sayi

sayi = int(input("Sayi giriniz: "))
print(faktoriyel(sayi)) 
