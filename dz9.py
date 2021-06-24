number1, number2, number3 = input('Enter the 3 numbers: ').split()
number1, number2, number3 = int(number1), int(number2), int(number3)

if number1 > number2:
    if number1 > number3:
        if number2 > number3:
            print(f'The middle number is {number2}')
        else:
            print(f'The middle number is {number3}')
    else:
        print(f'The middle number is {number1}')
elif number2 > number3:
    if number1 > number3:
        print(f'The middle number is {number1}')
    else:
            print(f'The middle number is {number3}')
else:
    print(f'The middle number is {number2}')
