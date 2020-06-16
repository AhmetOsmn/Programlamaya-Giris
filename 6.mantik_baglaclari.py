a = int(input("Birinci sayi: "))
b = int(input("Ikinci sayi: "))
c = int(input("Ucuncu sayi: "))

if(a == b == c):
    print("Uc sayi birbirine esittir.")
elif(a > b and a < c):
    print("Birinci sayi,ikinci sayi ile ucuncu sayi arasindadir.")
elif(a == b  and a < c):
    print("Birinci sayi,ikinci sayiya esittir ve ucuncu sayidan kucuktur.")
elif(a < b or a < c):
    print("Birinci sayi,ikinci sayidan veya ucuncu sayidan kucuktur.")
