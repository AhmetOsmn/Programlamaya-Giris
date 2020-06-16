
satir = [1,2,3,4,5]

#sayi = int(input("Sayi: "))

for i in range(1,6):
    satir.append(i)

#print(sutun)
#print(satir)

for i in range(1,6):
    a = []
    for j in range(0,5):
        a.append(i*satir[j])
    print(a)

print('x\t',end= '')
for i in range(1,11):
    print(i,end='\t')
print('')
for i in range(1,11):
    print(i,end='\t')
    for j in range(1,11):
        print(j*i,end='\t')
    print('')
