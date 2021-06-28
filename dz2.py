import random as rnd

ls1 = [int(rnd.random()*10) for i in range(10)]
ls2 = []

for i in range(len(ls1)):
    if ls1[i] % 2 == 0:
        ls2.append(i)

print(ls1)
print(ls2)
