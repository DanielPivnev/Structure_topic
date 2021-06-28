import random as rnd

ls1 = [int(rnd.random()*10) for i in range(10)]

min_digit_index = 0
max_digit_index = 0
for i in range(len(ls1)):
    if ls1[i] > ls1[max_digit_index]:
        max_digit_index = i
    elif ls1[i] < ls1[min_digit_index]:
        min_digit_index = i

ls1[min_digit_index], ls1[max_digit_index] = ls1[max_digit_index], ls1[min_digit_index]
