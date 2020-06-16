def rms(dizi):
    kareler = []
    for i in dizi:
        k = i**2
        kareler.append(k)
    #print(kareler)
    n = len(kareler)
    mean = sum(kareler)/n
    #print(mean)
    root = mean**(1/2)
    print(root)

dizi = [-2,5,-8,9,-4]
rms(dizi)
