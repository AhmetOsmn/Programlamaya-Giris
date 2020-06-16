a = int(input("1-100 arasinda bir sayi giriniz: "))

if(a >100 or a < 0 ):
    print("Gecersiz sayi.")
elif(a >= 90):
    print("A")
elif(a >= 80 and a < 90):
    print("B")
elif(a >= 70 and a < 80):
    print("C")
else:
    print("F")
