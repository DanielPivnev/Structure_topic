ls1 = []

for i in range(5):
    ls2 = []
    nums = input('Enter please a 3 numbers: ').split()
    for k in range(3):
        num = float(nums[k])
        ls2.append(num)
    ls2.append(sum(ls2))
    ls1.append(ls2)

max_lengths = [0, 0, 0, 0]
i = 0
for element in zip(ls1[0], ls1[1], ls1[2], ls1[3], ls1[4]):
    for j in range(len(element)):
        temporary_max_len = len(str(element[j]))
        if temporary_max_len > max_lengths[i]:
            max_lengths[i] = temporary_max_len
    i += 1

print('+—   ' + (' ' * sum(max_lengths)) + '—+')
for i in range(5):
    print('| ', end='')
    for j in range(4):
        while len(str(ls1[i][j])) != max_lengths[j]:
            if type(ls1[i][j]) != str:
                ls1[i][j] = str(ls1[i][j])
            ls1[i][j] = ' ' + ls1[i][j]
        print(ls1[i][j], ' ', end='')
    print('|')
print('+—   ' + (' ' * sum(max_lengths)) + '—+')
