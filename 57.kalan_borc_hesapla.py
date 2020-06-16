kredi = float(input("Çekilen kredi: "))
ay = int(input("Kaç ay: "))

odenecek = kredi + (kredi*9)/100
aylık = odenecek/ay
for i in range(3):
    odenecek -=  aylık
    print("Kalan Borcunuz: ",odenecek)
