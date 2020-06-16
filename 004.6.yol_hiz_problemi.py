mesafe = float(input("Mesafe (km): "))
ortalama_hiz = float(input("Ortalama Hiz (km/saat): "))

sure = mesafe / ortalama_hiz
sure = round(sure,2)
print("Varis suresi: {}'saattir.".format(sure))
