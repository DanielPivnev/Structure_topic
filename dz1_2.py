# Подсчитаваю, сколько было выделено памяти под переменные 4. домашнем задании 3-го урока.
# Версия Питона: 3.9
# ОC : macOS Big Sur (11.2.3)
# Процессор: 64 битовый

import random as rnd


ls1 = [int(rnd.random()*10) for i in range(100)]
ls2 = []


for i in range(len(ls1)):
    s = 0
    for j in range(len(ls1)):
        if ls1[i] == ls1[j]:
            s += 1
    ls2.append(s)

max_numbers_amount_index = ls2.index(max(ls2))

print(f'Most frequent numbers available = {ls1[max_numbers_amount_index]}')

#
# Размер ls1: Сами цифры --> 100 * 24 = 300 байта
#             Список --> 40 + 8 + 4 * 100 = 56 байтов
#             Итог --> 300 + 56 = 356 байтов
#
# Размер ls2: Сами цифры --> 100 * 24 = 300 байта
#             Список --> 40 + 8 + 4 * 100 = 56 байтов
#             Итог --> 300 + 56 = 356 байтов
#
# Размер max_numbers_amount_index: 1 * 24 = 3 байта
# ---------------------------------------------------
# Общий итог: 711 байтов
#
