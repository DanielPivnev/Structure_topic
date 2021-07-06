ls1 = []

for i in range(5):
    ls2 = []
    nums = input('Enter please a 3 numbers: ').split()
    for k in range(3):
        num = float(nums[k])
        ls2.append(num)
    ls2.append(sum(ls2))
    ls1.append(ls2)

max_lengths = []
max_len = 0
for list_2 in zip(ls1[0], ls1[1], ls1[2], ls1[3], ls1[4]):
    for j in range(len(list_2)):
        if len(str(list_2[j])) > max_len:
            max_len = len(str(list_2[j]))
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
