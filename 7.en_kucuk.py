a = int(input("Birinci sayi: "))
b = int(input("Ikinci sayi: "))
c = int(input("Ucuncu sayi: "))


if(a < b and a < c):
    print("Birinci sayi en kucuktur.")

elif(b < a and b < c):
    print("Ikınci sayi en kucuktur.")

elif(c < b and c < a):
    print("Ucuncu sayi en kucuktur.")
