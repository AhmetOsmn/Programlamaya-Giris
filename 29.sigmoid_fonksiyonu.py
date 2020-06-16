import math

sayi = float(input("Sayi: "))
sigmoid = 1/(1+math.exp(-sayi))
print(sigmoid)
