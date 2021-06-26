import random


number2 = random.randint(0, 100)
for _ in range(10):
    number = int(input('Guess the number: '))
    if number > number2:
        print('to big')
    elif number > number2:
        print('to big')
    else:
        print('you win')
        break
else:
    print('the number was:', number2)
