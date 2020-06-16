tarih1 = input("Tarih (xx.xx.xxxx): ")
tarih2 = input("Tarih (xx.xx.xxxx): ")

trh1 = tarih1.split(".")
trh2 = tarih2.split(".")

for i in range(3):
    trh1[i] = int(trh1[i])
    trh2[i] = int(trh2[i])

gun = abs(trh1[0] - trh2[0]) + 30*(abs(trh1[1] - trh2[1])) + 365 * (abs(trh1[2] - trh2[2]))

print(gun)
