a = int(input("Sayi: "))
for j in range(a):
    for i in range(a):
        if(i + j == a-1): #onemli
            print(1,end='')
        else:
            print(0,end='')
    print('')
