tarih = input("Tarih (xx.xx.xxxx): ")

aylar = ["","ocak","subat","mart","nisan","mayis","haziran","temmuz","agustos","eylül","ekim","kasim","aralik"]

bb = ["","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
ob = ["","on","yirmi","otuz","kirk","elli","altmis","yetmis","seksen","doksan"]
yb = ["","yuz","ikiyuz","ucyuz","dortyuz","besyuz","altiyuz","yediyuz","sekizyuz","dokuzyüz"]

binlerb = ["","bin","ikibin"]

trh = tarih.split(".")
for i in range (2):
    trh[i] = int(trh[i])

gun  = trh[0]
ay = trh[1]
yil = trh[2]
yil_basamak = []
for i in yil:
    yil_basamak.append(int(i))

gunn = ob[gun // 10] + bb[gun % 10]
ayy = aylar[ay]
yill = binlerb[yil_basamak[0]] + yb[yil_basamak[1]]+ ob[yil_basamak[2]] + bb[yil_basamak[3]]

print(gunn,ayy,yill)
