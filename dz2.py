number = int(input('Enter please a number: '))
even_numbers = []
odd_numbers = []

while number != 0:
    if (number % 10) % 2 == 0:
        even_numbers.append(number % 10)
    else:
        odd_numbers.append(number % 10)

    number = int(number / 10)


print(f'Even numbers - {even_numbers} \n'
      f'Odd numbers - {odd_numbers}')
