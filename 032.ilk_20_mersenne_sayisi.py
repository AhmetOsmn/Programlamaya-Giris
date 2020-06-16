#Mersenne sayilari : 2n-1 formulunden cikan sayilar.(1,3,7...)
def mersenne(n):
    return 2*n-1

mersenneler = []
i = 1
while(True):
    if(len(mersenneler) < 20):
        mersenneler.append(mersenne(i))
        i += 1
    else:
        break
print(mersenneler)
