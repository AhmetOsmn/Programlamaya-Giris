import math

sayi = float(input("Sayi: "))

tanh = (math.exp(sayi) - math.exp(-sayi))/(math.exp(sayi) + math.exp(-sayi))
print(tanh)
