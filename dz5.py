import random as rnd

ls1 = [int(rnd.random()*(-100)) for i in range(100)]

print(f'Position = {ls1.index(min(ls1))} \n'
      f'Number = {min(ls1)}')
