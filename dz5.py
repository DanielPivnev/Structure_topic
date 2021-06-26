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
