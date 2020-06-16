def aylarin_gun_sayisi(ay):
    if(ay == 1 or ay == 3 or ay == 5 or ay == 7 or ay == 8 or ay == 10 or ay == 12) :
        return 31
    elif(ay == 2):
        return 28
    elif(ay == 4 or ay == 6 or ay == 9 or ay == 11):
        return 30


print("Bugun icin tarihleri giriniz.(Gun.Ay.Yil)")
tarih1_gun = int(input("Gun: "))
tarih1_ay = int(input("Ay: "))
tarih1_yil = int(input("Yil: "))

print("Dogum gununuz icin tarihleri giriniz.(Gun.Ay.Yil)")
tarih2_gun = int(input("Gun: "))
tarih2_ay = int(input("Ay: "))
tarih2_yil = int(input("Yil: "))

gun_farki = abs(tarih1_gun - tarih2_gun)

aylardan_gun_farki = abs(aylarin_gun_sayisi(tarih1_ay) - aylarin_gun_sayisi(tarih2_ay))

yillardan_gun_farki = (tarih1_yil - tarih2_yil) * 365

ek_gun_sayisi = 0

while(tarih1_yil != tarih2_yil):
    if(tarih2_yil % 4 == 0):
        ek_gun_sayisi += 1
        tarih2_yil += 1
    else:
        tarih2_yil += 1


toplam_gun = (yillardan_gun_farki + aylardan_gun_farki + gun_farki + ek_gun_sayisi)


print("{}'gundur yasiyorsunuz tebriklerr...".format(toplam_gun))
#aos: 7324
#fb:7681
