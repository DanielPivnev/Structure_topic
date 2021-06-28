from random import randint as rnd


ls1 = [[rnd(0, 100) for j in range(10)] for i in range(5)]

min_elements = []
for i in range(len(ls1)):
    min_elements.append(min(ls1[i]))

print(max(min_elements))
