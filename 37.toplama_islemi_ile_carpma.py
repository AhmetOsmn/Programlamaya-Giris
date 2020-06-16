def manuel_carp(a,b):
    sonuc = 0
    for i in range(b):
        sonuc += a

    return sonuc

a = int(input("a: "))
b = int(input("b: "))

sonuc = manuel_carp(a,b)
print(sonuc)
