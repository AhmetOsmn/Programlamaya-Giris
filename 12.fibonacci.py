fib = [1,1]

sayi = int(input("Sayi: (sayi > 0)"))

if(sayi < 0):
    print("Gecersiz sayi...")

elif(sayi == 1 or sayi == 2):
    print(fib)
else:
    a = 1
    b = 1

    for i in range(0,sayi-1):
        c = a + b
        a,b = b,c
        fib.append(c)


    print(fib)
