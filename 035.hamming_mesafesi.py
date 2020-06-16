sayi1 = input("ikilik sistemde ayni bitte sayi giriniz(bosluksuz): ")
sayi2 = input("ikilik sistemde ayni bitte sayi giriniz(bosluksuz): ")

k = 0

if(sayi1 != sayi2):
    for i in range(len(sayi1)):
        if(sayi1[i] != sayi2[i]):
            k += 1

print("Hamming mesafesi: {}".format(k))
