import random


ls = [random.randint(-100, 100) for _ in range(100)]


def bubble_sort1(ls):
    n = len(ls)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls


def improved_bubble_sort(ls):
    max_sensible_idx = len(ls) - 1
    flag = False
    while True:
        for j in range(0, max_sensible_idx):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
                max_sensible_idx = j + 1
                flag = True
        if flag:
            flag = False
        else:
            break

    return ls



print(ls)
print(bubble_sort1(ls))
ls = [random.randint(-100, 100) for _ in range(100)]

print(ls)
print(improved_bubble_sort(ls))
