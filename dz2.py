import random


ls1 = [random.randint(-100, 100) for _ in range(10)]


def merge_sort(ls):
    middle_idx = int((len(ls)) / 2)

    def sort(half_ls, start, end):
        for i in range(start, end):
            if half_ls[i] > half_ls[i + 1]:
                j = i
                x = half_ls[i + 1]
                while j >= 0 and half_ls[j] > x:
                    half_ls[j + 1] = half_ls[j]
                    j -= 1
                if j < 0:
                    half_ls[start] = x
                else:
                    half_ls[j + 1] = x

    sort(ls, 0, middle_idx)
    sort(ls, middle_idx, len(ls) - 1)
    sort(ls, 0, len(ls) - 1)

    return ls


print(ls1)
print(merge_sort(ls1))
