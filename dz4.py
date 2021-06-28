import random as rnd

ls1 = [int(rnd.random()*10) for i in range(100)]
ls2 = []

for i in range(len(ls1)):
    s = 0
    for j in range(len(ls1)):
        if ls1[i] == ls1[j]:
            s += 1
    ls2.append(s)

max_numbers_amount_index = ls2.index(max(ls2))

print(f'Most frequent numbers available = {ls1[max_numbers_amount_index]}')
