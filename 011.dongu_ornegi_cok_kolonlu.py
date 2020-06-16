onbes = []
bes = []
on = []
iki_us = []
e = 100

for i in range(1,101):
    if(i % 15 == 0):
        onbes.append(i)
for i in range(1,31):
    if(i % 5 == 0):
        bes.append(i)
for i in range(1,7):
    iki_us.append(2 ** i)
while(e >49):
    if(e % 10 == 0):
        on.append(e)
    e -=1


"""
print(onbes)
print(bes)
print(on)
print(iki_us)
"""
for i in range(0,6):
    print(onbes[i],bes[i],on[i],iki_us[i])
