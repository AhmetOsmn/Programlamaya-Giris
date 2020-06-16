def manuel_carp_recursive(a,b):
    toplam = 0
    if(b == 1):
        return a

    toplam = a + manuel_carp_recursive(a,(b-1))
    return toplam

a = int(input("a: "))
b = int(input("b: "))

manuel_carp_recursive(a,b)

sonuc = manuel_carp_recursive(a,b)
print(sonuc)
