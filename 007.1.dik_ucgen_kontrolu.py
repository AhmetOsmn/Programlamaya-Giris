a = float(input("Ilk kenar: "))
b = float(input("Ikinci kenar: "))
c = float(input("Ucuncu kenar: "))

if((c**2) == (a**2) + (b**2)):
    print("Bu bir dik ucgendir.")

elif((b**2) == (a**2) + (c**2)):
    print("Bu bir dik ucgendir.")

elif((a**2) == (c**2) + (b**2)):
    print("Bu bir dik ucgendir.")

else:
    print("Bu bir dik ucgen degildir...")
