numbers = input('Please enter the numbers: ').split()
searched_digit = input('Please enter the digit: ')
searched_digit_quantity = 0

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if searched_digit == numbers[i][j]:
            searched_digit_quantity += 1

print(searched_digit_quantity)
