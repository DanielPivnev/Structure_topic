numbers = list(range(2, 100))
numbers2 = list(range(2, 10))
numbers3 = []

for i in range(len(numbers)):
    for j in range(len(numbers2)):
        if numbers[i] % numbers2[j] == 0:
            numbers3.append(numbers[i])

print(set(numbers3))
