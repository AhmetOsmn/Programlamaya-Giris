sayi = int(input("Ikilik sistemde sayi giriniz(Bosluksuz): "))

toplam = 0
ikinin_kati = 1
while(sayi > 0):
    bsd = int(sayi % 10)
    sayi /= 10
    toplam += ikinin_kati * bsd
    ikinin_kati *= 2

print(toplam)
