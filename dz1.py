
# ============================================================================ #
# Анализироваем скорость и сложность алгоритма из 4 домашнего задания 2 урока. #
# ============================================================================ #


import cProfile


# Цикл из урока
def for_print_chars():
    order = 32
    for i in range(10):
        sentence = '+————————————' * 10 + '+\n'
        for j in range(10):
            if order > 99 and order < 127:
                sentence += f'|  {order} - {chr(order)}   '
                order += 1
            if order <= 99:
                sentence += f'|   {order} - {chr(order)}   '
                order += 1
        print(sentence, '|', sep='')


# Улучшеный цикл
def for_print_chars2():
    order = 32
    for i in range(10):
        print('+————————————' * 10, '+', sep='')
        for j in range(10):
            if order <= 99:
                print(f'|   {order} - {chr(order)}   ', end='')
                order += 1
            elif 99 < order < 127:
                print(f'|  {order} - {chr(order)}   ', end='')
                order += 1
        print('|')


# Тоже самое с помочью рекурсии
def print_chars(from_order, to_order, column=0):
    if from_order < to_order:
        if column % 10 == 0:
            print('\n', ('+————————————' * 10), '+\n', '|', sep='', end='')
        if from_order <= 99:
            print(f'   {from_order} - {chr(from_order)}   |', end='')
        elif from_order > 99:
            print(f'  {from_order} - {chr(from_order)}   |', end='')
        print_chars(from_order+1, to_order, column+1)


def main():
    for_print_chars()
    print()
    for_print_chars2()
    print_chars(32, 127)


if __name__ == '__main__':
    cProfile.run('main()')

#
# 618 function calls (523 primitive calls) in 0.001 seconds
#
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 dz1.py:11(for_print_chars)
#         1    0.000    0.000    0.000    0.000 dz1.py:26(for_print_chars2)
#      96/1    0.000    0.000    0.001    0.001 dz1.py:41(print_chars)
#         1    0.000    0.000    0.001    0.001 dz1.py:52(main)
#       285    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       231    0.001    0.000    0.001    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# —————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Статистика показывает что for_print_chars() и for_print_chars2() на 0,001 секнду бистрее чем print_chars().
# Сама многа времине занимет built-in method builtins.exec по-этому print_chars() и медлиней.
#
