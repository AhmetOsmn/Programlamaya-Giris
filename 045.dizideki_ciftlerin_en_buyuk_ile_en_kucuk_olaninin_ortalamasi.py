import random
def ciftler(liste):
    ciftler = []
    for i in liste:
        if(i % 2 == 0):
            ciftler.append(i)
    return ciftler

def eb(liste):
    eb = 0
    for i in liste:
        if(i >= eb):
            eb = i
    return eb

def ek(liste):
    ek = liste[0]
    for i in liste:
        if(i <= ek):
            ek = i
    return ek

liste = []
for i in range(10):
    liste.append(random.randint(1,51))

print(liste)
ciftler = ciftler(liste)
eb = eb(ciftler)
ek = ek(ciftler)
ort = (eb + ek) / 2
print("Listedeki cift sayilarin en buyugu({}) ile en kucugunun({}) ortalamasi: {}".format(eb,ek,ort))
