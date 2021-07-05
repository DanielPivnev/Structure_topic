import collections


hexa_numbers_dict = collections.defaultdict(int)
hexa_numbers_list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
a = list(input('Pleas enter: ').upper())
b = list(input('Pleas enter: ').upper())
a_decimal = 0
b_decimal = 0
c_decimal = 0
c_mult = ''
c_add = ''
number = 15


def get_hexa_number(n, number=number, hnd=hexa_numbers_dict, hnl1=hexa_numbers_list1):
    hexa_numbers_list2 = []

    if n > number:

        while n >= number:
            max_len_hexa_numbers = max([len(x) for x in hnd.keys()])
            hexa_numbers_list2 = [x for x in hnd.keys() if len(x) == max_len_hexa_numbers]

            for i in range(1, 16):
                for j in range(len(hexa_numbers_list2)):
                    number += 1
                    hnd[hnl1[i] + hexa_numbers_list2[j]] = number

        return [x[0] for x in hnd.items() if x[1] == n][0]
    else:
         return [x[0] for x in hnd.items() if x[1] == n][0]


for i in range(16):
    hexa_numbers_dict[hexa_numbers_list1[i]] = i

for i in range(max(len(a), len(b))):
    if len(a) >= i:
        a_decimal += hexa_numbers_dict[a[i]]
    if len(b) >= i:
        b_decimal += hexa_numbers_dict[a[i]]

c_mult = get_hexa_number(a_decimal * b_decimal)
c_add = get_hexa_number(a_decimal + b_decimal)

print(f'Mult. : {c_mult}\n'
      f'Add.  : {c_add}')
