try:
    operator = ''
    while operator != '0':

        number1, number2 = input('Enter please two ingenious numbers: ').split()
        operator = input('Enter please a ingenious operator: ')

        # control the inputted numbers
        if ((number1[1:].isdigit() and number1[0] == '-' or number1.isdigit())
            or (('-' == number1.split('.')[0][0] and number1.split('.')[0][1:].isdigit())
                or (number1.split('.')[0].isdigit() and number1.split('.')[1].isdigit()))) \
            and ((number2[1:].isdigit() and number2[0] == '-' or number2.isdigit())
                or ('-' == number2.split('.')[0][0] and number2.split('.')[0][1:].isdigit())
                    or (number2.split('.')[0].isdigit() and number2.split('.')[1].isdigit())):

            # covert the numbers
            number1, number2 = float(number1), float(number2)
        else:
            # end the programm
            raise SyntaxError

        # control the inputted operator
        if operator in ['0', '*', '+', '/', '-']:

            # calculate
            if operator == '*':
                print(f'{number1} * {number2} = {round(number1 * number2, 8)}')
            elif operator == '/':
                if number1 == 0 or number2 == 0:
                    raise ZeroDivisionError
                else:
                    print(f'{number1} / {number2} = {round(number1 / number2, 8)}')
            elif operator == '-':
                print(f'{number1} - {number2} = {round(number1 - number2, 8)}')
            elif operator == '+':
                print(f'{number1} + {number2} = {round(number1 + number2, 8)}')

        else:
            while operator not in ['0', '*', '+', '/', '-']:
                operator = input('Enter please a legal ingenious operator ("0", "*", "+", "/", "-"): ')


except (SyntaxError, ZeroDivisionError) as e:
    print(e)
