import random as rnd


ls1 = [int(rnd.random()*100) for i in range(100)]

min_number1 = min(ls1)
ls1.remove(min_number1)
min_number2 = min(ls1)

print(f'{min_number1 = }\n'
      f'{min_number2 = }')
