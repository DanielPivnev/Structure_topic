
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
# Размер ls1: Сами строки --> 20 * длина * 37 = (92 байта + 4 бита) * длина
#             Список --> 40 + 8 + 4 * 20 = 16 байтов
#             Итог --> (92 байта + 4 бита) * длина + 16
#
# Размер max_lengths: Сами цифр --> 4 * 24 = 12 байтов
#                     Список --> 40 + 8 + 4 * 4 = 8 байтов
#                     Итог --> 12 байтов + 8 байтов = 20 байтов
#
# Размер max_len: 1 * 24 = 3 байта
# -------------------------------------------------------------------------
# Общий итог: (92 байта + 4 бита) * длина + 39 байтов
#
# -> Примечание: Можно было max_lengths и max_len в конце удалить
#
