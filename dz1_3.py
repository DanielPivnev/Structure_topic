
# Подсчитаваю, сколько было выделено памяти под переменные 4. домашнем задании 3-го урока.
# Версия Питона: 3.9
# ОC : macOS Big Sur (11.2.3)
# Процессор: 64 битовый

ls1 = []
ls2 = []

for i in range(5):
    ls2.clear()
    nums = input('Enter please a 3 numbers: ').split()
    for k in range(3):
        num = float(nums[k])
        ls2.append(num)
    ls2.append(sum(ls2))
    ls1.append(ls2)

max_lengths = []
max_len = 0
for inside_list in zip(ls1[0], ls1[1], ls1[2], ls1[3], ls1[4]):
    for j in range(len(inside_list)):
        if len(str(inside_list[j])) > max_len:
            max_len = len(str(inside_list[j]))
    max_lengths.append(max_len)

print('+—-' + (' ' * sum(max_lengths)) + ' -—+')
for i in range(5):
    print('| ', end='')
    for j in range(4):
        while len(str(ls1[i][j])) != max_lengths[j]:
            if type(ls1[i][j]) != str:
                ls1[i][j] = str(ls1[i][j])
            ls1[i][j] = ' ' + ls1[i][j]
        print(ls1[i][j], ' ', end='', sep='')
    print('|')
print('+—-' + (' ' * sum(max_lengths)) + ' -—+')

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
