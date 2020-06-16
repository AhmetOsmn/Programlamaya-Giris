def faktoriyel(sayi):

    if(sayi == 0):
        return 1

    elif(sayi == 1):
        return 1

    else:
        fakt = 1
        while(sayi != 1):
            fakt = fakt*sayi
            sayi -= 1

    return fakt

sayi = int(input("Sayi giriniz: "))
print(faktoriyel(sayi))
