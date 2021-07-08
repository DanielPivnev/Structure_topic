import random
import collections


ls = collections.deque([random.randint(0, 100) for _ in range(2 * 5 + 1)])
print(ls)

median_idx = round((len(ls) - 1) / 2)
median_element = ls[median_idx]
i = 0
while i < len(ls):
    if i < median_idx and ls[i] > median_element:
        ls.append(ls[i])
        del ls[i]
        median_idx -= 1
        i -= 1
    elif i > median_idx and ls[i] < median_element:
        ls.appendleft(ls[i])
        del ls[i + 1]
        median_idx += 1
        i += 1

    i += 1

print(ls)
