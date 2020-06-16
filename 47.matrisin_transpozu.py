def transpozAl(matris):
    sutun=[]
    sonMatris=[]
    s=0
    m=0
    while s < len(matris[0]): #ilk while döngüsü
       sutun=[]
       m=0
       while m < len(matris): #ikinci while döngüsü
            sutun.append(matris[m][s])
            m=m+1
       sonMatris.append(sutun)
       s=s+1
    return sonMatris

matris2 = [[2, 6, 5],[5, 6,8]]
for i in matris2:
    print (i)

print("-------")
for i in transpozAl(matris2):
    print (i)
