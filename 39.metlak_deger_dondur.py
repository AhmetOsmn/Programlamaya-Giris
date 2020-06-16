print("cikis icin 'q' tusuna basin.")
liste = []
while(True):
    sayi1 = input("Listeye eklenecek eleman (a,): ")
    if(sayi1 == "q"):
        break
    sayi2 = input("Listeye eklenecek eleman (,b): ")
    if(sayi2 == "q"):
        break
    demet = (int(sayi1),int(sayi2))
    liste.append(demet)
#print(liste)
mutlak_degerler = []

for i in liste:
    mutlak = max(i) - min(i)
    mutlak_degerler.append(mutlak)

for i in zip(liste,mutlak_degerler):
    print(i)
