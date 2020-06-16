saat = int(input("Suanki saat: "))
dakika = int(input("Suanki dakika: "))
fark = int(input("Fark (dakika):  "))

#print("Suanki saat: {}.{}".format(saat,dakika))

fark_saat = fark // 60
fark_dakika = fark - fark_saat * 60
#print(fark,fark_saat,fark_dakika)

yeni_dakika = fark_dakika + dakika
yeni_saat = fark_saat + saat

while(yeni_saat >= 24):
    yeni_saat -= 24

while(yeni_dakika >= 60):
    yeni_saat += 1
    yeni_dakika -= 60

print("Yeni saat: {}.{}".format(yeni_saat,yeni_dakika))
