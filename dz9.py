import math


numbers = input('Please enter the numbers: ').split()
max_digits = 0

for i in range(len(numbers)):
    numbers[i] = float(numbers[i])
    while numbers[i] % 1 != 0:
        numbers[i] = numbers[i] * 10
    numbers[i] = math.sqrt(numbers[i]**2)
    if max_digits < numbers[i]:
        max_digits = numbers[i]

print(len(str(int(max_digits))))
