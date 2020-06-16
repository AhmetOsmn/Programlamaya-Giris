def parca(a,b):
    l1 = []
    for i in a:
        for j in b:
            if(i == j):
                l1.append(j)
                b.remove(j)
                break
    #print(l1)
    if(l1 == a):
        print("Evet")
    else:
        print("Hayir")

parca( [1,2,2,2], [0,1,2,2,3,2,2])
