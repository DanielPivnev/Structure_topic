import random as rnd


ls1 = [int(rnd.random()*10) for i in range(100)]

min_number_index = ls1.index(min(ls1))
max_number_index = ls1.index(max(ls1))
sl = 0

if min_number_index > max_number_index:
    sl = slice(max_number_index, min_number_index + 1)
else:
    sl = slice(min_number_index + 1, max_number_index)

print(f'The sum of the elements between the minimum and maximum elements: {sum(ls1[sl])}')
