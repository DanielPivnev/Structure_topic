number = int(input('Please enter: '))
number2 = 1

if number == 1:
    print(1)
elif number > 1:
    for _ in range(number):
        number2 += number2 / -2
    print(number2)
else:
    print(0)
