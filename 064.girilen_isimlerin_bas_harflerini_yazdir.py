adet = int(input("Kac adet isim giriceksiniz: "))

isimler = []
for i in range(adet):
    isim = input("Isim giriniz: ")
    isimler.append(isim)

bas_harfler = []

for i in isimler:
    bas_harfler.append(i[0])

print("\n\nBas harfler: ")
for i in bas_harfler:
    print(i)
